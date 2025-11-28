import cv2 as cv

xpoints = []
ypoints = []

def mouseCallback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"x:{x}, y:{y}")
        xpoints.append(x)
        ypoints.append(y)

img = cv.imread("lab1/panZeStocka.jpg")

cv.namedWindow("window")
cv.setMouseCallback("window", mouseCallback)

while True:
    cv.imshow("window", img)
    if cv.waitKey(30) == ord("q"):
        break

    if len(xpoints) >= 2:
        roi = img[ypoints[0]:ypoints[1], xpoints[0]:xpoints[1]]

        negatyw = 255 - roi

        img[ypoints[0]:ypoints[1], xpoints[0]:xpoints[1]] = negatyw
        cv.imshow("window", img)
        cv.waitKey(0)
        break