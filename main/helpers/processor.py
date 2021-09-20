import cv2 as cv
import os
from django.conf import settings

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
            faceList.append(faceResized)
        return faceList
    
    def markFaces(self, coordList, img, color):
        for (x,y,w,h) in coordList:
            cv.rectangle(img,(x,y),(x+w,y+h),color,thickness=1)
        return img

