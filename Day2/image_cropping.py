import cv2
import numpy as np

img = cv2.imread('wallpaper.jpg')
cv2.imshow('original_image', img)
row,col,chan = img.shape
print('rows : ', row)
print('columns : ', col)

# Cropped image
cropped_image = img[100:500, 800:1100]
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#writing images
cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.imwrite('original_image.jpg', img)