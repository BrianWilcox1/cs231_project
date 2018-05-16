from __future__ import print_function

import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import sys, os
import png
import cv2
import shutil

cwd = os.getcwd()
Acount = 0
Bcount = 0
directory = os.path.join(cwd,'datasets','prostate')
testPathA = os.path.join(directory,'testA')
testPathB = os.path.join(directory,'testB')
trainPathA = os.path.join(directory,'trainA')
trainPathB = os.path.join(directory,'trainB')
if not os.path.exists(directory):
    os.makedirs(testPathA)
    os.makedirs(testPathB)
    os.makedirs(trainPathA)
    os.makedirs(trainPathB)
pathA = os.path.join(cwd,'T2')
pathB = os.path.join(cwd,'ADC')

for file in os.listdir(pathA):
    file_path = os.path.join(pathA,file)
    n = np.random.rand(1)
    if int(file[11:14]) <= 300:
        shutil.copy(file_path,trainPathA)

        #image path to be copied for flip
        img_path = trainPathA + '/' + file
    
    else:
        shutil.copy(file_path,testPathA)
        
        #image path to be copied for flip
        img_path = testPathA + '/' + file
        
    #functionality for making vertical copies of images
    img = cv2.imread(img_path)
    vertical_img = cv2.flip(img, 1 )
    file_path_b = img_path.replace(".png", "")
    file_path_b = file_path_b  + '_b.png'
    cv2.imwrite(file_path_b , vertical_img)
    
        
    Acount += 1
    print(Acount)
for file in os.listdir(pathB):
    file_path = os.path.join(pathB,file)
    n = np.random.rand(1)
    if int(file[11:14]) <= 300:
        shutil.copy(file_path,trainPathB)
        
        #image path to be copied for flip
        img_path = trainPathB + '/' + file
        
    else:
        shutil.copy(file_path,testPathB)
        
        #image path to be copied for flip
        img_path = testPathB + '/' + file
        
    #functionality for making vertical copies of images
    img = cv2.imread(img_path)
    vertical_img = cv2.flip(img, 1 )
    file_path_b = img_path.replace(".png", "")
    file_path_b = file_path_b  + '_b.png'
    cv2.imwrite(file_path_b , vertical_img)
        
    Bcount += 1
    print(Bcount)
    
