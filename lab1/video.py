import cv2 as cv

cap = cv.VideoCapture("lab1/Wildlife.mp4")

while True:
    ret, frame = cap.read()
    if not(ret):
        break

    cv.imshow("Window", frame)
    
    if cv.waitKey(5) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()