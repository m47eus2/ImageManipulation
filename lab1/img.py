import cv2 as cv
import sys
import numpy as np
 
img = cv.imread("lab1/panZeStocka.jpg")

print(np.shape(img))
print(img[100,100])
img[100:200, 100:200] = (255,0,0)
roi = img[500:600,500:600]
img[200:300, 200:300] = roi
img3 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Display window", img3)
cv.waitKey(0)