# -*- coding: utf-8 -*-
"""car_count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ZStlGxzMh9l-kFrIuRfq1JVqzRAqssy
"""

import time
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

import os 
import re

vidcap = cv2.VideoCapture('/content/Traffic in Bangalore is now a nuisance.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
      cv2.imwrite("/content/ Frames/"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

import os 
folder_path = "/content/ Frames/"
starttimevar = time.time()
l = []
for data_file in sorted(os.listdir(folder_path), key= natural_keys):
    im = cv2.imread(folder_path+'/'+data_file)
    #im = cv2.imread("/content/ Frames/76.jpg")
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    print('Number of cars in the ' +data_file +' is '+ str(label.count('car')))
    print('Number of cars in the ' +data_file +' is '+ str(label.count('bus')))
    print('Number of cars in the ' +data_file +' is '+ str(label.count('bicycle')))
    print('Number of cars in the ' +data_file +' is '+ str(label.count('motorbike')))
    print('Number of cars in the ' +data_file +' is '+ str(label.count('truck')))
    l.append(str(label.count('car')))
elapsetime = time.time() - starttimevar
print(elapsetime)
print(l)

