import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("lab1/panZeStocka.jpg")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

hist = cv.calcHist([imgGray],[0],None,[256],[0,256])

plt.figure()
plt.title("Histogram obrazu czarno-białego")
plt.plot(hist, color="black")
plt.xlim([0,256])

histChannels = []
histChannels.append(cv.calcHist([img],[0],None,[256],[0,256]))
histChannels.append(cv.calcHist([img],[1],None,[256],[0,256]))
histChannels.append(cv.calcHist([img],[2],None,[256],[0,256]))

plt.figure()
plt.title("Histogram obrazu kolorowego")
plt.plot(histChannels[0], color="blue")
plt.plot(histChannels[1], color="green")
plt.plot(histChannels[2], color="red")
plt.xlim([0,256])

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(imgGray)
cv.imshow("window", cl1)
cv.waitKey(0)

#plt.show()