import cv2
import numpy as np

img = cv2.imread('contour.jpg', cv2.IMREAD_GRAYSCALE)

# Threshold the image to binary
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours1, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw contours on a copy of the original image
img_contours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(img_contours, contours1, -1, (0, 255, 0), 2)
cv2.drawContours(img_contours, contours2, -1, (0, 0, 255), 1)
# Display the original and contour images
cv2.imshow('Original Image', img)
cv2.imshow('Contours Detected', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('contours_detected.jpg', img_contours)