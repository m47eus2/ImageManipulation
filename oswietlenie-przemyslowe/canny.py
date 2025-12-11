import cv2

def emptyCallback(value):
    pass

def main():
    cap = cv2.VideoCapture(0)  # open the default camera

    cv2.namedWindow("Canny");
    cv2.createTrackbar("Threshold1", "Canny", 1, 1000, emptyCallback)
    cv2.createTrackbar("Threshold2", "Canny", 1, 1000, emptyCallback)

    key = ord('a')
    while key != ord('q'):
        th1 = cv2.getTrackbarPos("Threshold1", "Canny")
        th2 = cv2.getTrackbarPos("Threshold2", "Canny")
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame comes here
        # Convert RGB image to grayscale
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur the image
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        # Detect edges on the blurred image
        img_edges = cv2.Canny(img_filtered, th1, th2)

        # Display the result of our processing
        cv2.imshow('Canny', img_edges)
        # Wait a little (30 ms) for a key press - this is required to refresh the image in our window
        key = cv2.waitKey(30)

    # When everything done, release the capture
    cap.release()
    # and destroy created windows, so that they are not left for the rest of the program
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()