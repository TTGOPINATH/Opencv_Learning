import cv2
import numpy as np

img = cv2.imread('excel.png')

# image filtering
kernal1 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
filtered_img = cv2.filter2D(img, -1, kernal1)


cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.imshow('Identity Filter', filtered_img)
cv2.waitKey(0)

# blur image
kernal2 = np.array([
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
    ])/25
#kernel2 = np.ones((5, 5), np.float32) / 25
blurred_img = cv2.filter2D(img, -1, kernal2)
cv2.imshow('Blurred Image', blurred_img)
cv2.waitKey(0)

# Bluring image using inbuilt function
blurred_img2 = cv2.blur(img, (5, 5))
cv2.imshow('Blurred Image 2', blurred_img2)
cv2.waitKey(0)
blurred_img3 = cv2.medianBlur(img, 5)
cv2.imshow('Median Blurred Image', blurred_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
