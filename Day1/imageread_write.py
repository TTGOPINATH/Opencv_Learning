# This code reads an image, converts it to grayscale,Color and Unchanged, displays it, and saves the grayscale image.
import cv2
import numpy as np
image = cv2.imread('excel.png',0)
image1 = cv2.imread('excel.png',1)
image2 = cv2.imread('excel.png',-1)
cv2.imshow('gray_image', image)
cv2.imshow('color_image', image1)
cv2.imshow('unchanged_image', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('excel_gray.png', image)
