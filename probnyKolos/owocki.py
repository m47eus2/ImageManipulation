import cv2 as cv
import numpy as np

def empty_callback(value):
    pass

img = cv.imread("probnyKolos/fruit.jpg")
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow('image')

cv.createTrackbar('LowH', 'image', 10, 255, empty_callback)
cv.createTrackbar('LowS', 'image', 10, 255, empty_callback)
cv.createTrackbar('LowV', 'image', 10, 255, empty_callback)
cv.createTrackbar('HighH', 'image', 200, 255, empty_callback)
cv.createTrackbar('HighS', 'image', 200, 255, empty_callback)
cv.createTrackbar('HighV', 'image', 200, 255, empty_callback)

while True:
    LH = cv.getTrackbarPos('LowH', 'image')
    LS = cv.getTrackbarPos('LowS', 'image')
    LV = cv.getTrackbarPos('LowV', 'image')
    HH = cv.getTrackbarPos('HighH', 'image')
    HS = cv.getTrackbarPos('HighS', 'image')
    HV = cv.getTrackbarPos('HighV', 'image')
    print(f"{LH}, {LS}, {LV}, {HH}, {HS}, {HV}")

    mask1 = cv.inRange(img_HSV, (22, 0, 0), (116, 78, 224))
    mask2 = cv.inRange(img_HSV, (0, 65, 129), (17, 149, 251))

    kernel = np.ones((10, 10), np.uint8)
    mask1D = cv.dilate(mask1, kernel, iterations=1)
    mask2D = cv.dilate(mask2, kernel, iterations=1)

    maskColor = np.zeros((mask1D.shape[0], mask1D.shape[1], 3), dtype=np.uint8)
    for i in range(0, mask1D.shape[0]):
        for j in range(0, mask1D.shape[1]):
            if(mask1D[i][j]==255):
                maskColor[i,j,:] = np.array((0,0,255), dtype=np.uint8)
    blended = cv.addWeighted(mask1D, 50, mask2D, 50, 0)
    
    
    

    cv.imshow('image', maskColor)

    if cv.waitKey(30)==ord('q'):
        break