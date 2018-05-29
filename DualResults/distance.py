### Requests input of 2 directory names from user (relative to the directory that this script resides)
### For all images in directory one, if there is a file with a matching name in directory two,
### The L1 and L2 distance is computed between pixels in both images.
### Data is output to file data_n.csv in the same folder as the script. 

from __future__ import print_function

import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import sys, os
import png
import cv2
import shutil

cwd = os.getcwd() #current directory 
#print(cwd)
var1 = input("Please enter the first directory name: ")
var2 = input("Please enter the second directory name: ")

pathA = os.path.join(cwd,var1)
pathB = os.path.join(cwd,var2)

if os.path.exists(pathA) == 0 or os.path.exists(pathB) == 0:
    print("Please refrain from entering imaginary directories, good sir")
    exit()
 
counter1 = 0 
counter2 = 0
for file in os.listdir(pathA):
    file1 = os.path.join(pathA,file)
    file2 = os.path.join(pathB,file)
    counter1 += 1
    if os.path.exists(file2):
        counter2+= 1
        
print("Directory1 has {} images".format(counter1))
print("Directory2 has {} matching images for comparison".format(counter2))

# Establish .csv output file for writing data   
counter = 0
while True:  
    name = "data_" + str(counter) + ".csv"
    if os.path.exists(name):
        print("Write file already exists...incrementing name")
        counter += 1
    else:
        break      
    
csv = open(name, "w") 
columnTitleRow = "Image name, L1_distance, L2_distance \n"
csv.write(columnTitleRow)

#compute L1/L2 distances between pairs of images and write data to output csv file
for file in os.listdir(pathA):
    file1 = os.path.join(pathA,file)
    file2 = os.path.join(pathB,file)
    if os.path.exists(file2):  #only continue if there is a matching image for comparison
        img1 = cv2.imread(file1)
        img2 = cv2.imread(file2)
        
        img1_vec = np.reshape(img1, (1, -1))
        img2_vec = np.reshape(img2, (1, -1))

        L1_norm = np.sum(abs(img1_vec - img2_vec)) 
        #print(img1_vec - img2_vec)
        #print(L1_norm)
        L2_norm = np.linalg.norm((img1_vec - img2_vec)) 
        
        
        Row = "{}, {}, {} \n".format(file, L1_norm, L2_norm)
        csv.write(Row)
  

    


