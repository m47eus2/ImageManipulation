import cv2 as cv

img = cv.imread("lab2/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)
th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Treasholded", th2)
cv.waitKey(0)