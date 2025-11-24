import cv2 as cv
import numpy as np
from time import perf_counter

class Timer:
    def getStartTime(self):
        self.startTime = perf_counter()
    def getStopTime(self):
        self.stopTime = perf_counter()
    def calcTime(self):
        return self.stopTime-self.startTime

manualTimer = Timer()
blurTimer = Timer()
filter2dTimer = Timer()

img = cv.imread("lab1/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)

# Co trzecia kolumna biała
for i in range(img.shape[1]):
    if(i%3==0): img[:,i] = 255

# Ręczne skanowanie
manualTimer.getStartTime()
filtered = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(i!=0 and i!=img.shape[0]-1 and j!=0 and j!=img.shape[1]-1):
            total = 0
            for a in range(3):
                for b in range(3):
                    total += int(img[i+(a-1), j+(b-1)])
            total = int(total / 9)
            filtered[i,j] = total
manualTimer.getStopTime()

# Blur
blurTimer.getStartTime()
blured = cv.blur(img, (3,3))
blurTimer.getStopTime()

# Filter2d
filter2dTimer.getStartTime()
kernel = np.ones((3,3), np.float32)/9
filtered2d = cv.filter2D(img, -1, kernel)
filter2dTimer.getStopTime()

print(f"Manual time: {manualTimer.calcTime()}")
print(f"Blur time: {blurTimer.calcTime()}")
print(f"Filter2D time: {filter2dTimer.calcTime()}")

cv.imshow("Manual", filtered)
cv.imshow("Blur", blured)
cv.imshow("Filter2D", filtered2d)

cv.waitKey(0)