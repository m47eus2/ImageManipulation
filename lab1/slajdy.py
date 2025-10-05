import cv2 as cv
import os

imgs=[]
dir = "lab1/slajdy"
imgnum = 0

for file in os.listdir(dir):
    imgs.append(cv.imread(f"lab1/slajdy/{file}"))

while True:
    cv.imshow("Window", imgs[imgnum])

    key = cv.waitKey(30)

    if key == ord("l"):
        imgnum += 1
        if imgnum>2: imgnum=0
    elif key == ord("h"):
        imgnum -= 1
        if imgnum<0: imgnum=2
    elif key == ord("q"):
        break

cv.destroyAllWindows()