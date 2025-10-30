import cv2 as cv
import numpy as np

img = cv.imread("lab1/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)

sobelx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype=np.float32)
sobely = np.array([[1,2,1],[0,0,0],[-1,-2,-1]], dtype=np.float32)
prewittx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]], dtype=np.float32)

sobelxImg = cv.filter2D(img, ddepth=cv.CV_64F, kernel=sobelx)
sobelyImg = cv.filter2D(img, ddepth=cv.CV_64F, kernel=sobely)

kolejnySobel = np.sqrt(sobelxImg*sobelxImg + sobelyImg*sobelyImg)
kolejnySobel = cv.convertScaleAbs(kolejnySobel)

#cv.imshow('Sobel', kolejnySobel)
#cv.waitKey(0)

cap = cv.VideoCapture(0)
key = ord('a')

while(key != ord('q')):
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    filtredx = cv.filter2D(frame, ddepth=cv.CV_64F, kernel=sobelx)
    filtredy = cv.filter2D(frame, ddepth=cv.CV_64F, kernel=sobely)
    filtred = np.sqrt(filtredx*filtredx + filtredy*filtredy)
    filtred = cv.convertScaleAbs(filtred)
    cv.imshow("okienko", filtred)
    key = cv.waitKey(30)