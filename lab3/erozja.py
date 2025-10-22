import cv2 as cv
import numpy as np

# Erozja -> biały obszar się zmniejsza

def emptyCallback(value):
    pass

img = cv.imread("lab2/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)
th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.namedWindow("Erozja");

cv.createTrackbar("Size", "Erozja", 1, 20, emptyCallback)

while(True):
    size = cv.getTrackbarPos("Size", "Erozja")
    if size<1: size=1

    kernel = np.ones((size, size), np.uint8)
    erosion = cv.erode(th, kernel, iterations=1)
    cv.imshow("Erozja", erosion) 

    if cv.waitKey(30)==ord('q'):
        break