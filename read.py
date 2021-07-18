import cv2 as cv


def readAndShowImage(imgFile, title):
    img = cv.imread(imgFile)
    cv.imshow(title,img)
    cv.waitKey(0)

def getFrameFromCamera():
    cap = cv.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        cv.imwrite('frames/frame{}.jpg'.format(count),frame) 
        count += 1
        cv.imshow("Frame", frame)
        t = cv.waitKey(1) 
        if t==27 or count >= 10:
            break
    cap.release()
    cv.destroyAllWindows()

getFrameFromCamera()
