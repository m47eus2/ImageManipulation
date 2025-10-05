import cv2 as cv

img = cv.imread("lab1/AdditiveColor.png")

#b,g,r = cv.split(img)

channels = []
for i in range(3):
    channels.append(img[:,:,i])

cv.imshow("B channel", channels[0])
cv.imshow("G channel", channels[1])
cv.imshow("R channel", channels[2])

cv.waitKey(0)