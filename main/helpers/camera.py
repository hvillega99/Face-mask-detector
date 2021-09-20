import cv2
from main.helpers import processor

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def getFrame(self):
        success, image = self.video.read()
        frameFlip = cv2.flip(image, 1)
        return frameFlip