# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:30:57 2021

@author: wgcotera
"""
# IMPORTS
# import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

# FUNCION PARA CAMBIAR A ESCALA DE GRISES A UNA IMAGEN DEL DIRECTORIO USANDO MATPLOTLIB

def toGris(direccion_img):
    imgRGB = mpimg.imread(direccion_img)
    # plt.imshow(imgRGB)
    R, G, B = imgRGB[:,:,0], imgRGB[:,:,1], imgRGB[:,:,2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    plt.imshow(imgGray, cmap='gray')
    return imgGray
    
# FUNCION PARA CAMBIAR A ESCALA DE GRISES A UNA IMAGEN DEL DIRECTORIO USANDO OpenCV

def toGray(direccion_img):
    imgRGB = cv2.imread(direccion_img)
    # cv2.imshow('Imagen a Color', imgRGB)
    imgGray = cv2.cvtColor(imgRGB,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagen Gris', imgGray)
    # k = cv2.waitKey(0)
    # if k==27:
    #     cv2.destroyAllWindows()
    # elif k==ord('s'):
    #     cv2.imwrite(direccion_img+'/1', imgRGB)
    #     cv2.destroyAllWindows()
    return imgGray

# FUNCION PARA AJUSTAR EL TAMAÑO DE UNA IMAGEN 

def toSize(direccion_img, dimX, dimY):
    img = cv2.imread(direccion_img)
    img = cv2.resize(img, (dimX, dimY), interpolation = cv2.INTER_CUBIC)
    # cv2.imshow('Img Tamaño nuevo', img)
    # cv2.waitKey(0)
    return img

# PRUEBAS
    
dir = "C:/Users/wgcot/TAWS/archive/data/without_mask/without_mask_25.jpg"
# imgGris = toGris(dir)
# imgGris = toGray(dir)
# print(imgGris)
# img = toSize(dir, 150, 200)
# print(img)
