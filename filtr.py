import cv2 as cv

def emptyCallback(value):
    pass

img1 = cv.imread("lab3/lenna_noise.bmp")
img2 = cv.imread("lab3/lenna_salt_and_pepper.bmp")

cv.namedWindow("Gauss")
cv.createTrackbar("Mask", "Gauss", 0, 100, emptyCallback)

cv.namedWindow("Median")
cv.createTrackbar("Mask", "Median", 0, 100, emptyCallback)

key = ord('a')
while key != ord('q'):
    mask = cv.getTrackbarPos("Mask", "Gauss")
    blur = cv.GaussianBlur(img1, (2*mask+1, 2*mask+1), 2)
    cv.imshow("Gauss", blur)

    mask = cv.getTrackbarPos("Mask", "Median")
    
    key = cv.waitKey(30)

