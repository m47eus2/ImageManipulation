import cv2 as cv
import numpy as np

def empty_callback(value):
    pass

cv.namedWindow("window")
cv.createTrackbar("Tile size", "window", 1, 100, empty_callback)
cv.createTrackbar("First color", "window", 0, 1, empty_callback)

while True:
    n = cv.getTrackbarPos("Tile size", "window")
    c = cv.getTrackbarPos("First color", "window")

    if n<1: n=1

    img = np.zeros((600,800), dtype=np.uint8)
    if c: img[:,:] = 255

    if(c): color = 0
    else: color = 255

    for i in range(0, img.shape[0], n):
        for j in range(0, img.shape[1], n):
            if(i//n + j//n)%2  != 0: img[i:i+n,j:j+n] = color

    cv.imshow("window", img)

    if cv.waitKey(30)==ord('q'):
        break