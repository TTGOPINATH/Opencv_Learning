import cv2
import numpy as np

img = cv2.imread('wallpaper.jpg')

#BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('BGR', img)
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)
cv2.imshow('RGB', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gray.jpg', gray)
cv2.imwrite('hsv.jpg', hsv)
cv2.imwrite('lab.jpg', lab)
cv2.imwrite('rgb.jpg', rgb)


