import cv2 as cv


img = cv.imread("lab5/drone_ship.jpg", cv.IMREAD_GRAYSCALE)

edges = cv.Canny(img, 881, 245)
cv.imshow("Canny", edges)
cv.waitKey(0)