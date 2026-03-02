import cv2
import numpy as np
image = cv2.imread('excel.png')
cv2.imshow('original_image', image)
#Downscale
down_width = 300
down_height = 200
down_points = (down_width, down_height)
down_image = cv2.resize(image, down_points, interpolation=cv2.INTER_AREA)
#upscale
up_width = 600
up_height = 400
up_points = (up_width, up_height)
up_image = cv2.resize(image, up_points, interpolation=cv2.INTER_CUBIC)
cv2.imshow('downscaled_image', down_image)
cv2.imshow('upscaled_image', up_image)
cv2.waitKey(0)
cv2.destroyAllWindows()