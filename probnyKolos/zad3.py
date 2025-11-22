import cv2 as cv
import numpy as np

xpoints = []
ypoints = []

def mouseCallback(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"x:{x}, y:{y}")
        xpoints.append(x)
        ypoints.append(y)
        
img = cv.imread("probnyKolos/jungle.jpg")
img = cv.resize(img, (0,0), fx=0.3, fy=0.3, interpolation=cv.INTER_AREA)

cv.namedWindow('window')
cv.setMouseCallback('window', mouseCallback)

while True:
    cv.imshow('window', img)
    if cv.waitKey(30) == ord('q'):
        break

    if len(xpoints) >= 2:
        roi = img[ypoints[0]:ypoints[1],xpoints[0]:xpoints[1]]
        roiFiltered = cv.GaussianBlur(roi, (21,21), 0)
        img[ypoints[0]:ypoints[1],xpoints[0]:xpoints[1]] = roiFiltered
        cv.imshow('window', img)
        cv.waitKey(0)
        break