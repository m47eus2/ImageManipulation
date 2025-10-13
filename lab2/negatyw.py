import cv2 as cv

img = cv.imread("lab2/panZeStocka.jpg", cv.IMREAD_COLOR)
negatyw = 255 -img
cv.imshow("window", negatyw)
cv.waitKey(0)