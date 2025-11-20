import cv2 as cv
import numpy as np

img = np.ones((600, 800, 3), dtype=np.uint8)*255

for i in range(0, img.shape[0], 3):
    for j in range(0, img.shape[1], 3):
        img[i,j,:] = np.array((0,0,255), dtype=np.uint8);

cv.imshow('window', img)
cv.waitKey(0)= np.array((0,0,255), dtype=np.uint8);= np.array((0,0,255), dtype=np.uint8);