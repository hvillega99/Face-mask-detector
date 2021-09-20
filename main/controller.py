from main.helpers.camera import VideoCamera
import cv2 as cv
from main.helpers import camera, processor

videoCamera = camera.VideoCamera()
faceProcessor = processor.FaceProcessor()

def getProcessedFrame():
    frame = videoCamera.getFrame()
    faces = faceProcessor.detectFaces(frame)
    markedFaces = faceProcessor.markFaces(faces, frame, (255, 0, 0))
    ret, jpeg = cv.imencode('.jpg', markedFaces)
    return jpeg.tobytes()