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

    maskApplesColor = cv.cvtColor(maskApples, cv.COLOR_GRAY2BGR)
    maskOrangesColor = cv.cvtColor(maskOranges, cv.COLOR_GRAY2BGR)

    circlesApples = cv.HoughCircles(maskApples, cv.HOUGH_GRADIENT, 1, 100,param1=10, param2=20, minRadius=0, maxRadius=0)
    circlesOranges = cv.HoughCircles(maskOranges, cv.HOUGH_GRADIENT, 1, 100,param1=10, param2=20, minRadius=0, maxRadius=0)

    res = img.copy()

    if circlesApples is not None:
        circlesApples = np.uint16(np.around(circlesApples))
        for x, y, r in circlesApples[0, :]:

            # prostokąt – niebieski
            cv.rectangle(res, (x - r, y - r), (x + r, y + r), (255, 0, 0), 2)

            # opcjonalnie: okręgi na podglądzie maski
            cv.circle(maskApplesColor, (x, y), r, (0, 255, 0), 2)
            cv.circle(maskApplesColor, (x, y), 2, (0, 0, 255), 3)


    if circlesOranges is not None:
        circlesOranges = np.uint16(np.around(circlesOranges))
        for x, y, r in circlesOranges[0, :]:

            # prostokąt – czerwony
            cv.rectangle(res, (x - r, y - r), (x + r, y + r), (0, 0, 255), 2)

            # opcjonalnie: okręgi na podglądzie maski
            cv.circle(maskOrangesColor, (x, y), r, (0, 255, 0), 2)
            cv.circle(maskOrangesColor, (x, y), 2, (0, 0, 255), 3)

    cv.imshow('image', res)

    if cv.waitKey(30) == ord('q'):
        break