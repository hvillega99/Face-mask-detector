""" from imutils.video import VideoStream
import imutils
import urllib.request """
import cv2
import os
from django.conf import settings
from main.helpers import processor

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.faceProcessor = processor.FaceProcessor()

    def __del__(self):
        self.video.release()

    def getFrame(self):
        success, image = self.video.read()
        frameFlip = cv2.flip(image, 1)
        faces = self.faceProcessor.detectFaces(frameFlip)
        finalFrame = self.faceProcessor.markFaces(faces, frameFlip, (255, 0, 0))
        ret, jpeg = cv2.imencode('.jpg', finalFrame)
        return jpeg.tobytes()