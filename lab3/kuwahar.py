import cv2 as cv
import numpy as np

img = cv.imread("lab1/panZeStocka.jpg", cv.IMREAD_GRAYSCALE)

filtered = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(i!=0 and i!=1 and i!=img.shape[0]-1 and i!=img.shape[0]-2 and j!=0 and j!=1 and j!=img.shape[1]-1 and j!=img.shape[1]-2):
            rois = []
            rois.append(img[i-2:i+1,j-2:j+1])
            rois.append(img[i-2:i+1,j:j+3])
            rois.append(img[i:i+3,j-2:j+1])
            rois.append(img[i:i+3,j:j+3])

            means = []
            stddevs = []

            for roi in rois:
                mean, stddev = cv.meanStdDev(roi)
                means.append(mean[0][0])
                stddevs.append(stddev[0][0])
            
            minIdx = 0
            minVal = stddevs[0]

            for k in range(len(stddevs)-1):
                if stddevs[k+1] < minVal:
                    minIdx = k
                    minVal = stddevs[k]

            filtered[i,j] = means[minIdx]

cv.imshow("Filtered", filtered)
cv.waitKey(0)