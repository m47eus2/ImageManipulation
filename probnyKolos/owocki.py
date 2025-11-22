import cv2 as cv
import numpy as np

def empty_callback(value):
    pass

img = cv.imread("probnyKolos/fruit.jpg")
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.namedWindow('image')

# cv.createTrackbar('LowH', 'image', 10, 255, empty_callback)
# cv.createTrackbar('LowS', 'image', 10, 255, empty_callback)
# cv.createTrackbar('LowV', 'image', 10, 255, empty_callback)
# cv.createTrackbar('HighH', 'image', 200, 255, empty_callback)
# cv.createTrackbar('HighS', 'image', 200, 255, empty_callback)
# cv.createTrackbar('HighV', 'image', 200, 255, empty_callback)

while True:
    # LH = cv.getTrackbarPos('LowH', 'image')
    # LS = cv.getTrackbarPos('LowS', 'image')
    # LV = cv.getTrackbarPos('LowV', 'image')
    # HH = cv.getTrackbarPos('HighH', 'image')
    # HS = cv.getTrackbarPos('HighS', 'image')
    # HV = cv.getTrackbarPos('HighV', 'image')
    # testMask = cv.inRange(img_HSV, (LH,LS,LV), (HH,HS,HV))

    maskApples = cv.inRange(img_HSV, (22, 0, 0), (116, 78, 224))
    maskOranges = cv.inRange(img_HSV, (0, 65, 129), (17, 149, 251))

    kernel = np.ones((6, 6), np.uint8)
    maskApples = cv.dilate(maskApples, kernel, iterations=1)
    maskOranges = cv.dilate(maskOranges, kernel, iterations=1)

    res = img.copy()
    res[maskOranges==255] = (0,0,255)
    res[maskApples==255] = (255,0,0)

    cv.imshow('image', res)

    if cv.waitKey(30)==ord('q'):
        break