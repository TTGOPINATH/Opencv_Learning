import cv2
import numpy as np

img = cv2.imread('wallpaper.jpg')
cv2.imshow('original_image', img)

# Image Rotation
height, width = img.shape[:2]
center = (width/2, height/2)
rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=90.0, scale=1.0)
rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow('rotated_image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()