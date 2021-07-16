import cv2 as cv


def readAndShowImage(imgFile, title):
    img = cv.imread(imgFile)
    cv.imshow(title,img)
    cv.waitKey(0)

def getVideoFromCamera():
    capture = cv.VideoCapture(0) 
    while True:
        isTrue, frame = capture.read()
        cv.imshow('video', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()

getVideoFromCamera()