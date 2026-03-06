import cv2
import numpy as np

vue = cv2.VideoCapture('video1.mp4')
# Background Subtraction
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = vue.read()
    if not ret:
        break
    fgmask = fgbg.apply(frame)
    # Display the original video and the foreground mask
    cv2.imshow('Original Video', frame)
    cv2.imshow('Foreground Mask', fgmask)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
vue.release()
cv2.destroyAllWindows()
cv2.imwrite('background_estimation.jpg', fgmask)