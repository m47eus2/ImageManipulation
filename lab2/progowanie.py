import cv2 as cv
import sys
import numpy as np
 
def empty_callback(value):
    pass

cv.namedWindow('image')
cv.createTrackbar('T', 'image', 0, 255, empty_callback)

img = cv.imread("lab2/panZeStocka.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

while True:
    cv.imshow('image', img_gray)

    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    # get current positions of four trackbars
    tresh = cv.getTrackbarPos('T', 'image')
    ret, th = cv.threshold(img_gray, tresh, 225, cv.THRESH_BINARY)
    cv.imshow('Progowanie', th)


# closes all windows (usually optional as the script ends anyway)
cv.destroyAllWindows()