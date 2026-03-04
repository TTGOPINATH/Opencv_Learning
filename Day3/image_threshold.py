import cv2
import numpy as np

img = cv2.imread('excel.png',0)

# 1. Binary Thresholding
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', thresh1)
cv2.waitKey(0)
# 2. Inverse Binary Thresholding
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse Binary Thresholding', thresh2)
cv2.waitKey(0)
# 3. Truncate Thresholding
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow('Truncate Thresholding', thresh3)
cv2.waitKey(0)
# 4. To Zero Thresholding
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow('To Zero Thresholding', thresh4)
cv2.waitKey(0)
# 5. Inverse To Zero Thresholding
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Inverse To Zero Thresholding', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()