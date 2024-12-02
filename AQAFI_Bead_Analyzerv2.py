# -*- coding: utf-8 -*-
"""
Copyright (c) 2022, Rutgers the State University of New Jersey, Muhammad Ahsan Sami, Muhammad Nabeel Tahir, and Umer Hassan
All rights reserved.
@authors: Muhammad Nabeel Tahir, Muhammad Ahsan Sami, Umer Hassan
@Emails: umer.hassan@rutgers.edu
@Date: Mon Sep 12 12:40:37 2022
@Disclaimer: The code is only intended for academic and research purposes. The distribution of the code and/or its modified versions is not allowed without the permission of the authors. 
The authors are not responsible for any potential loss or damage caused by the code. The code should not be used in commercial applications or any product development that could be sold.
"""

# -*- coding: utf-8 -*-

from ast import main

from array import array
import cv2
import csv
import numpy as np
import os
import pandas as pd


import matplotlib.pyplot as plt
# Creating an object of the Fast Feature detection class.
from sklearn.cluster import AgglomerativeClustering
#from photutils.centroids import centroid_sources, centroid_com
from Dataheaders import getSubDirs, Samples, Filters, Voltages, Sigmas



BeadsSize = [0.8, 1 , 2, 8]
n_bins = 255
UnfiltHeader = ['Bead',	'Sample' ,'Voltage',	'BeadInt',	'RingInt',	'NoiseInt', 'SDNR', 'CNR', 'SDNR_Mean', 'CNR_Mean', 'BeadInt_Mean', 'BeadInt_STD', 'RingInt_Mean', 'RingInt_STD', 'BeadCount']
UnfiltHeaderAve = ['Bead',	'Sample' ,'Voltage', 'NoiseInt',   'SDNR_Mean', 'CNR_Mean', 'BeadInt_Mean', 'RingInt_Mean', 'BeadCount']

# Function to generate the data files
def fileGen():
    
    #Creating csv data file for data storage
    with open('UnfiltData.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(UnfiltHeader)
    with open('UnfiltDataAve.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(UnfiltHeaderAve)




# Euclidean distance calculator function
def euclidian_distance(a, b):
    return np.linalg.norm(a - b)


"""
# Fast feature detection object with threshold 20. Smaller threshold will produce more features as  
# pixel p is a corner if there exists a set of n contiguous pixels in the circle (of 16 pixels) 
# which are all brighter than Ip+t, or all darker than Ip−t. (Shown as white dash lines in the above image). 
# n was chosen to be 12.
"""


"""
Method to get the file names when and initial location is given
The Input arguments are:
ImagePath: The base location of the data files.

Output Arguments:
filelist:  List of all files with absolute address.
"""
def getFileNames(ImagePath):
    result = []
    print(ImagePath)
    for root, dirs, files in os.walk(ImagePath):
        for filename in files:
            fname = os.path.join(root,filename)
            if fname.endswith('.jpg'):
                    result.append(fname)
    return result 

"""
The image path to the actual data. We run the AQAFI on the data of individual beads.
If there are multiple samplse just use the address ass
ImgBasePath = "C:.../AQAFI Code Base/Data/8 um Beads/
"""

# Change the name of the file accordingly and provide the complete path including the main directry file paths
ImgBasePath = "C:/Users/.../AQAFI Code Base/Data/8 um Beads/Sample 1/"
slicedelta = 35
"""
# Selecting the approperiate circle and euclidean distance for the feature clustering based on the size of the beads.
"""
def getHyperbeads(bsize):
    circleRadius  = 0
    d_threshold   = 0
    fastthreshold = 0

    if bsize ==8:
        circleRadius = 14  
        d_threshold  = 50   
        fastthreshold = 30
    elif bsize ==2:
        circleRadius = 6
        d_threshold  = 40
        fastthreshold = 20

    elif bsize ==1:
        circleRadius = 4
        d_threshold  = 24
        fastthreshold = 20

    elif bsize == 0.8:

        circleRadius = 4
        d_threshold  = 30

        fastthreshold = 13
        
    return (circleRadius, d_threshold, fastthreshold)
# Function to check if the box size is out of the picture size
def CoordChecker(coords):
    newcoords = coords.copy()
    newcoordsxu = coords[0]+slicedelta
    newcoordsxl = coords[0]-slicedelta
    newcoordsyu = coords[1]+slicedelta
    newcoordsyl = coords[1]-slicedelta
    if coords[0]+slicedelta>1080:
        newcoordsxu=1080
        newcoords[0] = 1080
    elif coords[0]-slicedelta<0:
        newcoordsxl=0
        newcoords[0] = 0
    if coords[1]+slicedelta>720:
        newcoordsyu=720
        newcoords[1] = 720
    elif coords[1]-slicedelta<0:
        newcoordsyl=0
        newcoords[1] = 0
    return (newcoordsxu, newcoordsxl, newcoordsyu,newcoordsyl, newcoords)


def FeatureSelector(featurecoords, Images):
    
    AvefeatintImage = (np.array(Images[:,:,0], dtype=float)+ np.array(Images[:,:,1], dtype=float) + np.array(Images[:,:,2], dtype=float))/3
   
    FeatureIntVect = AvefeatintImage[featurecoords[:,1], featurecoords[:,0]]
    featurintmean = np.mean(FeatureIntVect)
    featurintstd  = np.std(FeatureIntVect)

    tempfeaturecoords = np.where(FeatureIntVect>featurintmean-featurintstd) # Getting the coordinates of all the features which have intensity> mean-std

    newfeaturecoords=featurecoords[tempfeaturecoords,:][0]
  
    return newfeaturecoords



"""
Main Method that calculates the features using fast feature detection, clusters the points using clustering technique and then finally 
calculates the respective features (noise, bead, ring) intensities.
The Input arguments are:
ImagePath: The base location of the data files.

Output:
Data file containing all the information
"""
def getFeatures(ImgBasePath):
    #dg
    # Reading image using opencv
  
    for bead in BeadsSize:
        #ImagePath = ImgBasePath + str(bead) + ' um Beads/'
        bead =8
        circleRadius, d_threshold, fastthreshold=getHyperbeads(bead)
        
        
        files = getFileNames(ImgBasePath)
        print('Files',files)
        for f in files:
           
            BeadIntenarr = array('d')
            RingIntenarr = array('d')
            SDNRarr      = array('d')
            CNRarr       = array('d')
         
         
            fields = getSubDirs(f,bead)  
            print('Fields',(fields))
            if len(fields)==4:
                fastthreshold=22
            elif len(fields)==5:
                fastthreshold=22
            print('Fast Threshold', fastthreshold)
            fast = cv2.FastFeatureDetector_create(fastthreshold)
            print(f,' Length ',len(f))
            Img = cv2.imread(f)
            
            imS = cv2.resize(Img, (1080, 720))
            Imgnewfeatures = imS.copy()
            
            imgS = imS.copy()
            
            ## Applying fast feature detection algorithm
            kp = fast.detect(imS,None)
            if len(kp)==0:
                print('not detected')
            else:
                x = np.zeros(len(kp))
                y =  np.zeros(len(kp))
                coords = np.empty([len(kp),2], dtype=int)
                if(len(kp)>0):
                
                    i = 0
                    for point in kp:
                        x[i],y[i]=point.pt
                        img2 = cv2.circle(imS, (int(x[i]),int(y[i])), 3,(0,0,255))

                        coords[i]=[x[i],y[i]]
                        i+=1
            
                    cv2.imshow('Detected Image', imS)

                #cv2.imwrite()
                newfeatcoords = FeatureSelector(coords,imgS)
            
                
                clustering = AgglomerativeClustering(n_clusters=None,compute_full_tree=True, distance_threshold=d_threshold).fit(newfeatcoords)

                tempbeadint = 0
                tempringint = 0
                k = 0
                BeadDict = {}
                AveBeadDict = {}
                GausBeadDict = {}
                AvegDict ={}   
                for j in range(clustering.n_clusters_):
        
                    intenDict = {}
                
                    try:
                    
                        center_coord = np.mean(newfeatcoords[np.where(clustering.labels_==j)],axis=0, dtype=int)
                    except RuntimeWarning:
                        pass
        
        
                    newcoordsxu, newcoordsxl, newcoordsyu,newcoordsyl,newcoords = CoordChecker(center_coord)
                    
                    beadslice  = imgS[newcoordsyl:newcoordsyu, newcoordsxl:newcoordsxu]
                    
                    beadaveslice = (np.array(beadslice[:,:,0], dtype=int)+ np.array(beadslice[:,:,1], dtype=int) + np.array(beadslice[:,:,2], dtype=int))/3#cv2.cvtColor(beadslice, cv2.COLOR_BGR2GRAY)##
                    
                    flataveclice = beadaveslice.flatten()
            
                    beadint = np.mean(flataveclice[flataveclice>=int(np.percentile( flataveclice,99))])#int(np.amax(grayslice))

                    img3 = cv2.circle(imgS, (center_coord), circleRadius,(0,0,0), -1)
                    ringslice  = img3[newcoordsyl:newcoordsyu, newcoordsxl:newcoordsxu]

                    averingslice = (np.array(ringslice[:,:,0], dtype=int)+ np.array(ringslice[:,:,1], dtype=int) + np.array(ringslice[:,:,2], dtype=int))/3#cv2.cvtColor(ringslice, cv2.COLOR_BGR2GRAY)#

                    averingslice = averingslice[averingslice>0]
                    meanaveringslice = np.mean(averingslice)
                    stdaveringslice = np.std(averingslice)
                    updateaveringslice = averingslice[averingslice<meanaveringslice+2*stdaveringslice]
                    #print(updateaveringslice.shape)
                    # circlearea = int(np.pi*circleRadius*circleRadius)
                    # print('Ring slice no of pixel', averingslice.size)
                    # print(circlearea)
                    # tempbeadint+=beadint
                    ringint = np.mean(updateaveringslice)
                    
                    BeadIntenarr.append(beadint)
                    RingIntenarr.append(ringint)
                    SDNRarr.append((beadint-ringint))
                    if ringint==0:
                        ringint=1
                    CNRarr.append((beadint-ringint)/(ringint))
                    tempringint+=ringint
                    
                    
                cv2.imshow('Before Box Centers Image', img3)
                imgcirc = img3.copy()
                for j in range(clustering.n_clusters_):
                    center_coord = np.mean(newfeatcoords[np.where(clustering.labels_==j)],axis=0, dtype=int)
                    newcoordsxu, newcoordsxl, newcoordsyu,newcoordsyl,newcoords = CoordChecker(center_coord)
                    img3 = cv2.rectangle(img3, (newcoordsxl,newcoordsyu),(newcoordsxu, newcoordsyl),(0,0,0), -1)
    
            

                print('Complete Image Mean',np.mean(Img))

                AveImage = (np.array(img3[:,:,0], dtype=float)+ np.array(img3[:,:,1], dtype=float) + np.array(img3[:,:,2], dtype=float))/3#cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)##cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

                noisemean = (np.mean(AveImage))
                noisestd = (np.std(AveImage))
                flattenImg3 = AveImage.flatten().copy()
                # Updating the noise estimate
                flattenImg1 = flattenImg3[flattenImg3<(noisemean+noisestd)]
                noisemean = (np.mean(flattenImg1))
                noisestd = (np.std(flattenImg1))

                BeadIntenarr = np.array(BeadIntenarr)
                RingIntenarr = np.array(RingIntenarr)
                #print('Bead Array', len(BeadIntenarr))
                #print(BeadIntenarr[BeadIntenarr<noisemean+2*noisestd])
                #Updating the bead intensity array
                TempBeadIntarray = BeadIntenarr[BeadIntenarr>noisemean+2*noisestd]
                #print('Temp Bead Array', len(TempBeadIntarray))
                # Updating the bead count
                Beadcount = len(TempBeadIntarray)
                print('No. of Beads Detected',Beadcount)
                #Updating the Ring intensity array
                TempRingIntarray = RingIntenarr[np.where(BeadIntenarr>noisemean+2*noisestd)]
                
                SDNRarr=np.array(SDNRarr)
                #Updating the SDNR array
                SDNRarr=SDNRarr[np.where(BeadIntenarr>noisemean+2*noisestd)]
                
                CNRarr = np.array(CNRarr)
                #Updating the CNR array
                CNRarr=CNRarr[np.where(BeadIntenarr>noisemean+2*noisestd)]
                SDNRarr/=noisemean
                CNRarr/=noisemean
                
                #print('UnFiltered',flattenImg3.shape)
                flattenImg1=0
                k=0
                
    
                print('Average Bead Int', np.mean(TempBeadIntarray))
                print('Average Ring Int', np.mean(TempRingIntarray))
                print('SDNR', np.mean(SDNRarr))
                print('CNR', np.mean(CNRarr))
                print('Noise', noisemean)
                print('Noise std', noisestd)
                #print('1STD mean', np.mean(flattenImg1))
                testDict = {1:'0'} 
                
                if len(fields)==2:
        
                    #FiltDict['Orig'] = BeadDict
                    #MainDict[str(bead)][fields[0]][fields[-1]] = testDict
                    BeadDict['Bead'] = bead
                    BeadDict['Sample'] = fields[0]
                    BeadDict['Voltage'] = fields[-1]
                    
                    BeadDict['BeadInt']=TempBeadIntarray
                    BeadDict['RingInt']=TempRingIntarray
                    BeadDict['NoiseInt'] = noisemean
                    BeadDict['SDNR']    = SDNRarr
                    BeadDict['CNR']    =  CNRarr
                    BeadDict['SDNR_Mean'] = np.mean(SDNRarr)
                    BeadDict['CNR_Mean'] = np.mean(CNRarr)
                    BeadDict['BeadInt_Mean']=np.mean(TempBeadIntarray)
                    BeadDict['BeadInt_STD']=np.std(TempBeadIntarray)
                    BeadDict['RingInt_Mean']=np.mean(TempRingIntarray)
                    BeadDict['RingInt_STD']=np.std(TempRingIntarray)
                    BeadDict['BeadCount']   =   Beadcount

                    AvegDict['Bead']=bead
                    AvegDict['Sample'] = fields[0]
                    AvegDict['Voltage'] = fields[-1]
                    AvegDict['NoiseInt'] = noisemean
                    AvegDict['SDNR_Mean'] = np.mean(SDNRarr)
                    AvegDict['CNR_Mean'] = np.mean(CNRarr)
                    AvegDict['BeadInt_Mean']=np.mean(TempBeadIntarray)
                    AvegDict['RingInt_Mean']=np.mean(TempRingIntarray)
                    AvegDict['BeadCount']   =   Beadcount

                    dfave = pd.DataFrame(AvegDict, index=[0])
                    dfave.to_csv('UnfiltDataAve.csv',mode='a', index=False, header=False)
                    df = pd.DataFrame(BeadDict)
                    df.to_csv('UnfiltData.csv',mode='a', index=False, header=False)
                    # VoltDict[fields[-1]] = BeadDict
                    # SampleDict[fields[0]] = VoltDict
                
                cv2.imshow('Detected Centers Image', img3)
                k = cv2.waitKey(0)
                if( k == ord('c') ):
                    cv2.imwrite('Images/'+fields[0]+'_'+str(bead)+'_'+fields[-1]+'.png', imS)
                    cv2.imwrite('Images/'+fields[0]+'_'+str(bead)+'_bead_'+fields[-1]+'.png', imgcirc)
                    cv2.imwrite('Images/'+fields[0]+'_'+str(bead)+'_box_'+fields[-1]+'.png', img3)
                    print("Image is saved color")
                
                          
                           
                # closing all open windows
                cv2.destroyAllWindows()    
            
            
        break
            
   
if __name__ == "__main__":
    print('Main')
    fileGen()
    getFeatures(ImgBasePath)
