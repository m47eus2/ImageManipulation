import cv2 as cv
import sys
import numpy as np
import time
 
img = cv.imread("lab2/qr.jpg")

start = time.time()
img2 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_LINEAR)
end = time.time()
timeLinear = end-start

start = time.time()
img3 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_NEAREST)
end = time.time()
timeNearest = end-start

start = time.time()
img4 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_AREA)
end = time.time()
timeArea = end-start

start = time.time()
img5 = cv.resize(img, (0,0), fx=2.75, fy=2.75, interpolation=cv.INTER_LANCZOS4)
end = time.time()
timeLanczos4 = end-start

print(f"Linear scaling time: {timeLinear}")
print(f"Nearest scaling time: {timeNearest}")
print(f"Area scaling time: {timeArea}")
print(f"Lanczos4 scaling time: {timeLanczos4}")

cv.imshow("Display window", img2)
cv.waitKey(0)