import cv2
import numpy as np

img = cv2.imread('image_1.jpg',0)
equalized_img = cv2.equalizeHist(img)
cv2.imshow('Original Image', img)
cv2.imshow('Histogram Equalization', equalized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('equalized_image.jpg', equalized_img)