import cv2 as cv

def emptyCallback(value):
    pass

img = cv.imread("lab3/lenna_salt_and_pepper.bmp")
cv.namedWindow("Median Blur");

cv.createTrackbar("Size", "Median Blur", 1, 30, emptyCallback)

while(True):
    size = cv.getTrackbarPos("Size", "Median Blur")
    if size<1: size=1
    filtered = cv.medianBlur(img, (size*2)-1)
    cv.imshow("Median Blur", filtered) 

    if cv.waitKey(30)==ord('q'):
        break