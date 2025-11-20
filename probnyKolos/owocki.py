import cv2 as cv

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

    frame_threshold = cv.inRange(img_HSV, (LH, LS, LV), (HH, HS, HV))
    cv.imshow('image', frame_threshold)

    if cv.waitKey(30)==ord('q'):
        break