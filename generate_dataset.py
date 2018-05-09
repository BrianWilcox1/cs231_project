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
    else:
        shutil.copy(file_path,testPathA)
    Acount += 1
    print(Acount)
for file in os.listdir(pathB):
    file_path = os.path.join(pathB,file)
    n = np.random.rand(1)
    if int(file[11:14]) <= 300:
        shutil.copy(file_path,trainPathB)
    else:
        shutil.copy(file_path,testPathB)
    Bcount += 1
    print(Bcount)
    
