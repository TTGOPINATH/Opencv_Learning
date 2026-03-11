import cv2
import numpy as np

# Load the image
image = cv2.imread('image_1.jpg')
#copy the image to display the corners
image_copy = image.copy()
# Convert the image to grayscale
gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
# Detect corners using the Harris corner detection method
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
# Dilate the corner points to enhance them
corners = cv2.dilate(corners, None)
# Threshold the corner points to identify strong corners
image[corners > 0.01 * corners.max()] = [0, 0, 255]
cv2.imshow('Original Image', image)
cv2.imshow('Feature Detection', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()