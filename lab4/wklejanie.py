import cv2 as cv
import numpy as np

xpoints = []
ypoints = []

def mouseCallback(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"x:{x}, y:{y}")
        xpoints.append(x)
        ypoints.append(y)

img = cv.imread('lab4/road.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
print(img.shape)
cv.namedWindow('image')
cv.setMouseCallback('image',mouseCallback)

while(True):
    if len(xpoints) >= 4:
        pts1 = np.float32([[0,0], [1280,0],[0,800],[1280,800]])
        pts2 = np.float32([[xpoints[0], ypoints[0]], [xpoints[1],ypoints[1]],[xpoints[2],ypoints[2]],[xpoints[3],ypoints[3]]])
        M = cv.getPerspectiveTransform(pts1, pts2)
        dst = cv.warpPerspective(img, M, (1280,800))

        cv.imshow('image', dst)
        cv.waitKey(0)
        break


    cv.imshow('image', img)
    if cv.waitKey(30)==ord('q'):
        break