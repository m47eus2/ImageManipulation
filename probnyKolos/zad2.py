import cv2 as cv
import numpy as np

img = np.ones((600, 800, 3), dtype=np.uint8)*255

for i in range(0, img.shape[0]):
    if(i%3==0):
        img[i,:,:] = (0,0,255)

for i in range(0, img.shape[1]):
    if(i%3==0):
        img[:,i,:] = (0,0,255)

filtered = cv.GaussianBlur(img, (5,5), 0.8)

cv.imshow('window', filtered)
cv.waitKey(0)