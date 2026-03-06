import cv2
import numpy as np

img = cv2.imread('contour.jpg',0)

# Background Subtraction
fgbg = cv2.createBackgroundSubtractorMOG2()
fgmask = fgbg.apply(img)
# Display the original image and the foreground mask
cv2.imshow('Original Image', img)
cv2.imshow('Foreground Mask', fgmask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('background_estimation.jpg', fgmask)