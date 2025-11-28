import cv2 as cv
import numpy as np

def empty_callback(value):
    pass

cv.namedWindow("window")
cv.createTrackbar("Poziom R", "window", 0, 255, empty_callback)
cv.createTrackbar("Poziom G", "window", 0, 255, empty_callback)

while True:
    r = cv.getTrackbarPos("Poziom R", "window")
    g = cv.getTrackbarPos("Poziom G", "window")

    n=25

    img = np.zeros((500,500,3), dtype=np.uint8)

    for i in range(0, img.shape[0], n):
        for j in range(0, img.shape[1], n):
            if(i//n + j//n)%2  != 0: img[i:i+n,j:j+n] = (0,0,r)
            else: img[i:i+n,j:j+n] = (0,g,0)

    cv.imshow("window", img)

    if cv.waitKey(30)==ord('q'):
        break