### Requests input of 2 directory names from user (relative to the directory that this script resides)
### For selected image in the generated GAN data set, the script returns the nearest neighbor from the training dataset.
### Both images are copied and saved in the same directory as neighbor.py file. 
### This file should be run right outside of the two directories of images that are being compared. 

from __future__ import print_function

import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import sys, os
import png
import cv2
import shutil
import skimage.io as io

cwd = os.getcwd() #current directory 
#print(cwd)
var1 = input("Please enter the first directory name in quotes (GAN generated images): ")
var2 = input("Please enter the second directory name in quotes (Training Dataset): ")
var3 = input("Which image number from the GAN generated data set would you like to use? This is zero indexed.")

var3 = int(var3)

pathA = os.path.join(cwd,var1)
pathB = os.path.join(cwd,var2)

if os.path.exists(pathA) == 0 or os.path.exists(pathB) == 0:
    print("Please refrain from entering imaginary directories, good sir")
    exit()
 


#compute L2 distances to find nearest neighbor of desired input image
image_number = 0
for file in os.listdir(pathA):

    if image_number == var3:   #only find nearest neighbor for desired training image, as input by user
        print("Chose image {} from GAN generated data set!".format(file))
        file1 = os.path.join(pathA,file)
        img1 = cv2.imread(file1, 0) #read training image as grayscale
        
        #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        #cv2.imshow( "image", img1)
       
        
        nearest_value_l1 = float('Inf')
        nearest_value_l2 = float('Inf')
        for file in os.listdir(pathB):
            file2 = os.path.join(pathB,file)            
            img2 = cv2.imread(file2, 0) #read GAN generated image as grayscale
                
            img1_vec = np.reshape(img1, (1, -1))
            img2_vec = np.reshape(img2, (1, -1))

            L1_norm = np.sum(abs(img1_vec - img2_vec)) 
            #print(img1_vec - img2_vec)
            #print(L1_norm)
            L2_norm = np.linalg.norm((img1_vec - img2_vec)) 
            #print(L2_norm)
            if L1_norm < nearest_value_l1:
                nearest_value_l1 = L1_norm
                nearest_file_l1 = file
                nearest_img_l1 = img2
                #print("Updated Nearest Neighbor!")

            if L2_norm < nearest_value_l2:
                nearest_value_l2 = L2_norm
                nearest_file_l2 = file
                nearest_img_l2 = img2
                #print("Updated Nearest Neighbor!")
                
                

    image_number += 1 #increment image number

print("Final nearest L1 neighbor from training set is: {}".format(nearest_file_l1))
print("Final nearest L2 neighbor from training set is: {}".format(nearest_file_l2))
print("Final Manhatten (L1) distance for nearest neighbor is: {} ".format(nearest_value_l1))
print("Final Euclidian (L2) distance for nearest neighbor is: {} ".format(nearest_value_l2))


file_out1 = os.path.join(cwd, "GAN_neighbor_image.png")
file_out2 = os.path.join(cwd, "training_"+"L1"+".png")
file_out3 = os.path.join(cwd, "training_"+"L2"+".png")

 
#print(file_out1)
#print(file_out2)

cv2.imwrite(file_out1 , img1)
cv2.imwrite(file_out2 , nearest_img_l1)
cv2.imwrite(file_out3 , nearest_img_l2)

    


