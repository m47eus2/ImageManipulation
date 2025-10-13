import cv2 as cv

def emptyCallback(value):
    pass

cv.namedWindow("blending")
cv.createTrackbar("WeightA", "blending", 0, 100, emptyCallback)
cv.createTrackbar("WeightB", "blending", 0, 100, emptyCallback)
cv.createTrackbar("Gamma", "blending", 0, 100, emptyCallback)

im1 = cv.imread("lab2/panZeStocka.jpg")
im2 = cv.imread("lab2/PUTVISION_LOGO.png")
im2 = cv.resize(im2, dsize=(im1.shape[1], im1.shape[0]))

while True:
    weightA = cv.getTrackbarPos("WeightA", "blending")/100
    weightB = cv.getTrackbarPos("WeightB", "blending")/100
    gamma = cv.getTrackbarPos("Gamma", "blending")
    blended = cv.addWeighted(im1, weightA, im2, weightB, gamma)

    cv.imshow("blending", blended)

    key = cv.waitKey(30)
    if key == 27:
        break