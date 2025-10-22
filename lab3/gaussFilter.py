import cv2 as cv

def emptyCallback(value):
    pass

img = cv.imread("lab3/lenna_noise.bmp")
cv.namedWindow("Gauss filter");

cv.createTrackbar("Size", "Gauss filter", 1, 100, emptyCallback)
cv.createTrackbar("Weight", "Gauss filter", 1, 100, emptyCallback)

while(True):
    size = cv.getTrackbarPos("Size", "Gauss filter")
    weight = cv.getTrackbarPos("Weight", "Gauss filter")

    if size<1: size=1
    if weight<1: weight=1
    filtered = cv.GaussianBlur(img, ((size*2)-1, (size*2)-1), weight/10.0)
    cv.imshow("Gauss filter", filtered) 

    if cv.waitKey(30)==ord('q'):
        break