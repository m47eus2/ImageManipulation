import cv2 as cv
import numpy as np

xpoints = []
ypoints = []

def mouseCallback(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"x:{x}, y:{y}")
        xpoints.append(x)
        ypoints.append(y)

baseImg = cv.imread("lab1/panZeStocka.jpg")

img = cv.imread('lab4/road.jpg')
img = cv.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

cv.namedWindow('image')
cv.setMouseCallback('image',mouseCallback)

while(True):
    if len(xpoints) >= 4:
        pts1 = np.float32([[0,0], [img.shape[1],0],[0,img.shape[0]],[img.shape[1],img.shape[0]]])
        pts2 = np.float32([[xpoints[0], ypoints[0]], [xpoints[1],ypoints[1]],[xpoints[2],ypoints[2]],[xpoints[3],ypoints[3]]])
        M = cv.getPerspectiveTransform(pts1, pts2)
        dst = cv.warpPerspective(img, M, (baseImg.shape[1],baseImg.shape[0]))

        dstGray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
        ret, dstMask = cv.threshold(dstGray, 0, 255, cv.THRESH_BINARY)
        dstMaskInv = cv.bitwise_not(dstMask)

        baseImg = cv.bitwise_and(baseImg, baseImg, mask=dstMaskInv)
        frontImg = cv.bitwise_and(dst, dst, mask=dstMask)

        blended = cv.add(baseImg, frontImg)

        cv.imshow('image', blended)
        cv.waitKey(0)
        break


    cv.imshow('image', baseImg)
    if cv.waitKey(30)==ord('q'):
        break