from __future__ import print_function

import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import sys, os
import png
import cv2

cwd = os.getcwd()
count = 0
adc_count = 0
t2_count =0
for folder, subdirList, fileList in os.walk(cwd):
    if folder[-9:-6] == 'ADC' or folder[-9:-6] == 'tra':
        print(count)
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(folder)
        reader.SetFileNames(dicom_names)

        image = reader.Execute()

        array = np.array(sitk.GetArrayFromImage(image))
        count += 1
        for i in range(array.shape[0]):
            fname = os.path.join(cwd,folder,folder[-9:-6]+str(i)+'.png')
            max_val = np.amax(array[i,:,:])
            png_array = (array[i,:,:]/ float(max_val) * 255.0).astype(int)
            if folder[-9:-6] == 'ADC':
                H,W = png_array.shape
                h = int(H/2)
                w = int(W/2)
                step = 33
                png_array = png_array[h-step:h+step,w-step:w+step]
            else:
                H,W = png_array.shape
                h = int(H/2)
                w = int(W/2)
                step = 125
                png_array = png_array[h-step:h+step,w-step:w+step]
            plt.imsave(fname,png_array,cmap='gray')
        for i in range(array.shape[0]):
            fname = folder+'/'+folder[-9:-6]+str(i)+'.png'
            try:
                if folder[-9:-6] == 'ADC':
                    directory = os.path.join(cwd,'ADC')
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    im = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
                    resized = cv2.resize(im,(256,256),interpolation = cv2.INTER_CUBIC)
                    plt.imsave(os.path.join(directory,folder[-9:-6]+str(adc_count)+'.png'),resized,cmap='gray')
                    adc_count += 1
                else:
                    directory = os.path.join(cwd,'T2')
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    im = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
                    resized = cv2.resize(im,(256,256),interpolation = cv2.INTER_CUBIC)
                    plt.imsave(os.path.join(directory,folder[-9:-6]+str(t2_count)+'.png'),resized,cmap='gray')
                    t2_count += 1
            except:
                pass