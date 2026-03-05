import cv2
import numpy as np

img = cv2.imread('BlobTest.jpg', cv2.IMREAD_GRAYSCALE)
img_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

#edge detection using sobel operator
sobelx = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img_gaussian, cv2.CV_64F, 0, 1, ksize=5)
sobelxy = cv2.Sobel(img_gaussian,cv2.CV_64F,1,1,ksize=5)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel XY', sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sobelx.jpg', sobelx)
cv2.imwrite('sobely.jpg', sobely)
cv2.imwrite('sobelxy.jpg', sobelxy)

#canny edge detection
edges = cv2.Canny(img_gaussian, 200, 300)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('canny_edges.jpg', edges)