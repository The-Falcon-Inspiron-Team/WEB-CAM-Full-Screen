import cv2
cap = cv2.VideoCapture(0)

cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    success, image = cap.read()

    cv2.imshow("Image", image)

    if cv2.waitKey(1) == ord('q'): 
      break


cv2.destroyAllWindows()
cap.release()