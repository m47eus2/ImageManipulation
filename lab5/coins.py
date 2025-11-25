import cv2 as cv
import numpy as np

img = cv.imread("lab5/coins.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,50,param1=500,param2=50,minRadius=30,maxRadius=150)
circles = np.uint16(np.around(circles))

total = 0

for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    #print(i[2])

    if (95 < i[2] < 115): total += 100
    if (40 < i[2] < 60): total += 10

total /= 100
print(f"{total:.2f}")
cv.imshow("Circles", cimg)
cv.waitKey(0)