
"""
Copyright (c) 2022, Rutgers the State University of New Jersey, Muhammad Ahsan Sami, Muhammad Nabeel Tahir, and Umer Hassan
All rights reserved.
@authors: Muhammad Nabeel Tahir, Muhammad Ahsan Sami, Umer Hassan
@Emails: umer.hassan@rutgers.edu
@Date: Mon Sep 12 12:40:37 2022
@Disclaimer: The code is only intended for academic and research purposes. The distribution of the code and/or its modified versions is not allowed without the permission of the authors. 
The authors are not responsible for any potential loss or damage caused by the code. The code should not be used in commercial applications or any product development that could be sold.
"""

import numpy as np

Samples = ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4']
Filters = ['Average', 'Gaussian']
Voltages = ['4_3', '4_4', '4_5']
Sigmas = ['sig_1', 'sig_3', 'sig_5']


"""
Method to get the file names sample number, filter, voltages, and sigmas
The Input arguments are:
ImagePath: The location of the data files.

Output Arguments:
fields:  Tuple with all the information.
"""
def getSubDirs(fileName,bead):
    if Samples[0] in fileName:
        print(fileName)
        field = (Samples[0], fileName[-7:-4])   

        if Filters[0] in fileName:
            if Voltages[0] in fileName:
                if bead ==0.8:
                    if len(fileName)==103:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[0])
                else:
                    if len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==99:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[0])

            elif Voltages[1] in fileName:
                if bead ==0.8:
                    if len(fileName)==103:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[1])
                else:
                    if len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==99:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[1])

            elif Voltages[2] in fileName:
                if bead==0.8:

                    if len(fileName)==103:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[2])
                else:
                    if len(fileName)==101:
                        field = (Samples[0],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==99:
                        field = (Samples[0],Filters[0], fileName[-11:-8],Voltages[2])

            
        elif Filters[1] in fileName:
            if Voltages[0] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])

                elif Sigmas[1] in fileName:
                    if bead==0.8:

                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])

                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
     
            elif Voltages[1] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])

                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                    
            elif Voltages[2] in fileName:
                if Sigmas[0] in fileName:
                     if bead==0.8:

                            if len(fileName)==112:
                                   field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])
                     else:
                            if len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==108:
                                   field = (Samples[0],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])

                elif Sigmas[1] in fileName:
                     if bead==0.8:

                            if len(fileName)==112:
                                   field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])
                     else:
                            if len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==108:
                                   field = (Samples[0],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])

                elif Sigmas[2] in fileName:
                     if bead==0.8:

                            if len(fileName)==112:
                                   field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])
                     else:
                            if len(fileName)==110:
                                   field = (Samples[0],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                            elif len(fileName)==108:
                                   field = (Samples[0],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])

    elif Samples[1] in fileName:
        field = (Samples[1], fileName[-7:-4])   

        if Filters[0] in fileName:
            if Voltages[0] in fileName:
                if bead==0.8:

                    if len(fileName)==103:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[0])
                else:
                    if len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==99:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[0])

            elif Voltages[1] in fileName:
                if bead==0.8:

                    if len(fileName)==103:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[1])
                else:
                    if len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==99:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[1])
                
            elif Voltages[2] in fileName:
                if bead ==0.8:
                    if len(fileName)==103:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[2])
                else:
                    if len(fileName)==101:
                        field = (Samples[1],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==99:
                        field = (Samples[1],Filters[0], fileName[-11:-8],Voltages[2])
                    
        elif Filters[1] in fileName:
            if Voltages[0] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])
                    
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
                        
            elif Voltages[1] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])
                        
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                        
            elif Voltages[2] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])
                        
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[1],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])
                        
    elif Samples[2] in fileName:
        field = (Samples[2], fileName[-7:-4])   

        if Filters[0] in fileName:
            if Voltages[0] in fileName:
                if bead==0.8:
                    if len(fileName)==103:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[0])
                else:
                    if len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[0])
                    elif len(fileName)==99:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[0])
                
            elif Voltages[1] in fileName:
                if bead==0.8:
                    if len(fileName)==103:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[1])
                else:
                    if len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[1])
                    elif len(fileName)==99:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[1])
                    
            elif Voltages[2] in fileName:
                if bead==0.8:
                    if len(fileName)==103:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[2])
                else:
                    if len(fileName)==101:
                        field = (Samples[2],Filters[0], fileName[-13:-8],Voltages[2])
                    elif len(fileName)==99:
                        field = (Samples[2],Filters[0], fileName[-11:-8],Voltages[2])

        elif Filters[1] in fileName:
            if Voltages[0] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[0])
                        
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[0])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[0])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[0])
                        
            elif Voltages[1] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:

                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[1])
                        
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[1])
                        
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[1])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[1])
                    
            elif Voltages[2] in fileName:
                if Sigmas[0] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[0], fileName[-13:-10], Voltages[2])
                    
                elif Sigmas[1] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[1], fileName[-13:-10], Voltages[2])
                       
                elif Sigmas[2] in fileName:
                    if bead==0.8:
                        if len(fileName)==112:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])
                    else:
                        if len(fileName)==110:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-15:-10], Voltages[2])
                        elif len(fileName)==108:
                            field = (Samples[2],Filters[1], Sigmas[2], fileName[-13:-10], Voltages[2])
        
    elif Samples[3] in fileName:
        field = (Samples[2], fileName[-7:-4])  

    return field