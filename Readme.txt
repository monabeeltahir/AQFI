Please Cite the work as M. A. Sami, M. N. Tahir, and U. Hassan, “Aqafi: a bioanalytical method
for automated kpis quantification of fluorescent images of human leukocytes
and micro–nano particles,” Analyst, vol. 148, pp. 6036–6049, 2023. [Online].
Available: http://dx.doi.org/10.1039/D3AN01166F

Copyright (c) 2022, Rutgers the State University of New Jersey, Muhammad Ahsan Sami, Muhammad Nabeel Tahir, and Umer Hassan
All rights reserved.
@authors: Muhammad Nabeel Tahir, Muhammad Ahsan Sami, Umer Hassan
@Emails: nabeel.tahir@rutgers.edu
@Date: Mon Sep 12 12:40:37 2022
@Disclaimer: The code is only intended for academic and research purposes. The distribution of the code and/or its modified versions is not allowed without the permission of the authors. 
The authors are not responsible for any potential loss or damage caused by the code. The code should not be used in commercial applications or any product development that could be sold.


This folder contains three Python files, one data folder, and two generated results files.

How to run:

The main AQAFI_Bead_Analyzerv2 file was used to apply the AQFI method to the collected data. A sample data file has also been provided in the data folder.
To run the file, install the pre-requisite libraries listed at the top of the AQAFI_Bead_Analyzerv2 file and change the value of the ImagePath variable to the exact location
of the extracted folder in your directory, including the main directory path.

The Dataheader file extracts the relevant subfolders and directories in the main data folder and provides the values to the main function.

The UnfiltData and AveUnfiltData files provide the information and estimated values of all the variables listed in the paper for each bead detected in an image and the overall 
average of these variables for all beads detected in an image.


