import cv2 as cv

def emptyCallback(value):
    pass

#img = cv.imread("lab1/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)
img = cv.imread("lab5/drone_ship.jpg", cv.IMREAD_GRAYSCALE)
cv.namedWindow("Canny");

cv.createTrackbar("Threshold1", "Canny", 1, 1000, emptyCallback)
cv.createTrackbar("Threshold2", "Canny", 1, 1000, emptyCallback)

while(True):
    th1 = cv.getTrackbarPos("Threshold1", "Canny")
    th2 = cv.getTrackbarPos("Threshold2", "Canny")

    edges = cv.Canny(img, th1, th2)
    cv.imshow("Canny", edges)

    if cv.waitKey(30)==ord('q'):
        break