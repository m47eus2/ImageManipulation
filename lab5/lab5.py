import cv2 as cv
import numpy as np

img = cv.imread("lab1/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)

sobelx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype=np.float32)
sobely = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], dtype=np.float32)
prewittx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]], dtype=np.float32)

filx = cv.filter2D(img, ddepth=cv.CV_64F, kernel=sobelx) / 4
fily = cv.filter2D(img, ddepth=cv.CV_64F, kernel=sobely) / 4

fil = np.sqrt(filx*filx + fily*fily) / 255

#cv.imshow('Sobel', fil)
#cv.waitKey(0)

cap = cv.VideoCapture(0)
key = ord('a')

while(key != ord('q')):
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    filtredx = cv.filter2D(frame, ddepth=cv.CV_64F, kernel=sobelx) / 4
    filtredy = cv.filter2D(frame, ddepth=cv.CV_64F, kernel=sobely) / 4
    filtred = np.sqrt(filtredx*filtredx + filtredy*filtredy) / 255
    #filtred = cv.convertScaleAbs(filtred)
    cv.imshow("okienko", filtred)
    key = cv.waitKey(30)