import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import cv2

def thresholding_func(img, thv):
    
    img2 = np.zeros(img.shape)
    
    for i in range(0,len(img[:,0])):
        for j in range(0,len(img[0])):
            if img[i][j] <= thv:
                img2[i][j] = 0
            elif img[i][j] > thv:
                img2[i][j] = 255
                
    return img2 

def data_generator(thv):
    
    img_data =  np.zeros([len(thv),448,448])
    
    for i in range(len(thv)):
        name = thv['Name'][i]
        img = cv2.imread('images/' + name + '.tif',0)
        img_data[i] = img[0:448,0:448]
        
    print("Shape of 2D Data Generated: ",img_data.shape)
    
    return img_data

def data_generator3D(thv):
    
    img_data =  np.zeros([len(thv),448,448,3])
    
    for i in range(len(thv)):
        name = thv['Name'][i]
        img = cv2.imread('images/' + name + '.tif')
        img_data[i] = img[0:448,0:448,:]
        
    print("Shape of 3D Data Generated: ",img_data.shape)
    
    return img_data

def size_reduction(tensor, size=(100,100)):
    
    image_data = np.zeros((len(tensor),100,100))
    
    for i in range(len(tensor)):
        image_data[i] = cv2.resize(tensor[i],size, interpolation = cv2.INTER_AREA)
    
    return image_data