import cv2 as cv
import sys
import numpy as np
 
img = cv.imread("lab2/qr.jpg")
img2 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_LINEAR)
img3 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_NEAREST)
img4 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_AREA)
img5 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_LANCZOS4)
cv.imshow("Display window", img5)
cv.waitKey(0)