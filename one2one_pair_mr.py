from __future__ import print_function

import matplotlib.pyplot as plt
import SimpleITK as sitk
import numpy as np
import sys, os
import png
import cv2
import shutil
from os import listdir
from os.path import isfile, join

# place this script in the datasets/prostate/ directory

def check_on2one(directory_A, directory_B):

    cwd = os.getcwd()
    pathA = join(cwd,directory_A)
    pathA_files = [extract(f) for f in listdir(pathA) if isfile(join(pathA, f))]
    pathB = join(cwd,directory_B)
    pathB_files = [extract(f) for f in listdir(pathB) if isfile(join(pathB, f))]
    interAB_list = list(set(pathA_files) & set(pathB_files))

    (fileA_list,fileB_list) = expand_fname(interAB_list)

    return (fileA_list,fileB_list)
    

def extract(fname):
    fname = fname.replace('.png','')
    fname = fname.replace('ProstateX-','')
    fname = fname.replace('tra','+')
    fname = fname.replace('ADC','+')
    return fname

def expand_fname(flist):
    fileA_list = [expand(f,ADC=False) for f in flist]
    fileB_list = [expand(f,ADC=True) for f in flist]
    return(fileA_list,fileB_list)


def expand(fname,ADC=True):
    if ADC == True:
        fname = fname.replace('+','ADC')
    else:
        fname = fname.replace('+','tra')
    fname = 'ProstateX-'+fname+'.png'
    return fname

def generate_one2one_dataset(directoriesA, directoriesB):

    for i in np.arange(len(directoriesA)):
        fileA_list,fileB_list = check_on2one(directoriesA[i], directoriesB[i])
        cwd = os.getcwd()
        Acount = 0
        Bcount = 0

        directory = os.path.join(cwd,'datasets','prostate')
        dest_PathA = os.path.join(directory,directoriesA[i])
        dest_PathB = os.path.join(directory,directoriesB[i])

        if not os.path.exists(dest_PathA):
            os.makedirs(dest_PathA)
            os.makedirs(dest_PathB)
        pathA = os.path.join(cwd,directoriesA[i])
        pathB = os.path.join(cwd,directoriesB[i])

        for file in fileA_list:
            new_fname = file.replace('tra','')
            file_path = os.path.join(pathA,file)
            shutil.copy(file_path,os.path.join(dest_PathA,new_fname))
            Acount += 1
            print(Acount)

        for file in fileB_list:
            new_fname = file.replace('ADC','')
            file_path = os.path.join(pathB,file)
            shutil.copy(file_path,os.path.join(dest_PathB,new_fname))
            Bcount += 1
            print(Bcount)

if __name__ == '__main__':
    directoriesA = ['trainA','testA']
    directoriesB = ['trainB','testB']
    generate_one2one_dataset(directoriesA, directoriesB)