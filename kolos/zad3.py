import cv2 as cv
import random
import numpy as np

xpoints = []
ypoints = []


def mouseCallback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"x:{x}, y:{y}")
        xpoints.append(x)
        ypoints.append(y)


img = cv.imread('kolos/fredzia_phi_phi.png')

cv.namedWindow('window')
cv.setMouseCallback('window', mouseCallback)

while True:
    cv.imshow('window', img)
    if cv.waitKey(30) == ord('q'):
        break

    if len(xpoints) > 0:
        color = img[ypoints[0],xpoints[0]]
        print(color)

        randomB = random.randint(0, 255)
        randomG = random.randint(0, 255)
        randomR = random.randint(0, 255)

        # Pierwsze rozwiązanie z pętlą
        #
        # res = np.zeros_like(img)
        # for i in range(img.shape[0]):
        #     for j in range(img.shape[1]):
        #         if img[i,j,0] == color[0] and img[i,j,1]==color[1] and img[i,j,2]==color[2]:
        #             res[i,j] = (randomB, randomG, randomR)
        #         else: res[i,j] = img[i,j,:]


        # Drugie rozwiązanie z maskami
        maskB = np.zeros_like(img)
        maskG = np.zeros_like(img)
        maskR = np.zeros_like(img)

        maskB = cv.cvtColor(maskB, cv.COLOR_BGR2GRAY)
        maskG = cv.cvtColor(maskG, cv.COLOR_BGR2GRAY)
        maskR = cv.cvtColor(maskR, cv.COLOR_BGR2GRAY)

        bCh, gCh, rCh = cv.split(img)

        maskB[bCh == color[0]] = 255
        maskG[gCh == color[1]] = 255
        maskR[rCh == color[2]] = 255

        mask = cv.bitwise_and(maskB, maskG, maskR)

        res = img.copy()
        res[mask==255] = (randomB, randomG, randomR)

        cv.imshow('window', res)
        cv.waitKey(0)
        break