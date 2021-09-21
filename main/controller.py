import cv2 as cv
import os
from main.helpers import camera, processor
import joblib
from django.conf import settings
import numpy as np

videoCamera = camera.VideoCamera()
faceProcessor = processor.FaceProcessor()
modelPath = os.path.join(settings.BASE_DIR, 'main/models/face_detection_SVM_COLOR.h5')
svm = joblib.load(modelPath)

def getProcessedFrame():
    frame = videoCamera.getFrame()
    faces = faceProcessor.detectFaces(frame)
    X = faceProcessor.getFacesProcessed(faces, frame)
    y = []
    markedFaces = frame
    if len(X) > 0:
        y = svm.predict(X)
        for index in range(len(y)):
            if y[index]:
                markedFaces = faceProcessor.markFaces(faces[index], markedFaces, (0, 255, 0))
            else:
                markedFaces = faceProcessor.markFaces(faces[index], markedFaces, (0, 0, 255))
    ret, jpeg = cv.imencode('.jpg', markedFaces)
    return jpeg.tobytes()