import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('14depth.avi')
#fg = cv.bgsegm.createBackgroundSubtractorMOG()

while cap.isOpened():
    ret, frame = cap.read()
    cv.imshow('original Frame', frame)
    if ret == True:

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #fgmask = fg.apply(frame)
        _, th1 = cv.threshold(gray, 175, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        cv.imshow('Threshold', th1)
        #cv.imshow('FG Frame', fgmask)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()