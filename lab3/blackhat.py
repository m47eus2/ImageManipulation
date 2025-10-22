import cv2 as cv
import numpy as np

# Blackhat -> różnica pomiędzy zamknięciem a oryginałem (robi coś w rodzaju negatywu, mniej białego)

def emptyCallback(value):
    pass

img = cv.imread("lab2/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)
th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.namedWindow("Window");

cv.createTrackbar("Size", "Window", 1, 20, emptyCallback)

while(True):
    size = cv.getTrackbarPos("Size", "Window")
    if size<1: size=1

    kernel = np.ones((size, size), np.uint8)
    dilation = cv.morphologyEx(th, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("Window", dilation) 

    if cv.waitKey(30)==ord('q'):
        break