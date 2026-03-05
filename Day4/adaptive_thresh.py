import cv2
import numpy as np

img = cv2.imread('excel.png', cv2.IMREAD_GRAYSCALE)

#Adaptive Thresholding
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.imshow('Adaptive Mean Thresholding', thresh1)  
cv2.waitKey(0)
cv2.imshow('Adaptive Gaussian Thresholding', thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()