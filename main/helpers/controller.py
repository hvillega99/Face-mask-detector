import cv2 as cv

def resize(img, dimX = 150, dimY = 200):
    imgResized = cv.resize(img, (dimX, dimY), interpolation = cv.INTER_CUBIC)
    return imgResized

