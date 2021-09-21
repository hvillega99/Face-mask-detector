import cv2 as cv
import os
from django.conf import settings
from numpy import asanyarray, array

class FaceProcessor:
    def __init__(self):
        self.haar_cascade = cv.CascadeClassifier(os.path.join(settings.BASE_DIR, 'main/models/haar_face.xml'))

    def detectFaces(self, img):
        return self.haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=8)

    def getFacesProcessed(self, coordList, img):
        faceList = []
        for (x,y,w,h) in coordList:
            face = img[y:y+h,x:x+w]
            faceResized = cv.resize(face, (150, 200), interpolation = cv.INTER_CUBIC)
            faceArr = asanyarray(faceResized).reshape(-1)
            faceList.append(faceArr)
        return array(faceList)
    
    def markFaces(self, coordList, img, color):
        x,y,w,h = coordList
        cv.rectangle(img,(x,y),(x+w,y+h),color,thickness=2)
        """ for (x,y,w,h) in coordList:
            cv.rectangle(img,(x,y),(x+w,y+h),color,thickness=2) """
        return img
    

