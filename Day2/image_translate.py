import cv2
import numpy as np

img = cv2.imread('wallpaper.jpg')
height,width,_ = img.shape[:2]

# Define the translation matrix
tx,ty = width/6, height/6
translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
trans_img = cv2.warpAffine(img, translation_matrix, (width, height))
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image', trans_img)
cv2.waitKey(0)
