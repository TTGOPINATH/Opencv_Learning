import cv2
import numpy as np

img = cv2.imread('image_1.jpg')
# Define the source points (corners of the original image)
src_pt = np.float32([[0, 0], [img.shape[1], 0], [img.shape[1], img.shape[0]], [0, img.shape[0]]])
# Define the destination points (corners of the warped image)
dst_pt = np.float32([[50, 50], [img.shape[1] - 30, 30], [img.shape[1] - 30, img.shape[0] - 50], [30, img.shape[0] - 30]])
# Compute the perspective transformation matrix
M = cv2.getPerspectiveTransform(src_pt, dst_pt)
# Warp the image using the perspective transformation
warped_img = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
cv2.imwrite('warped_image.jpg', warped_img)
cv2.imshow('Original Image', img)
cv2.imshow('Warped Image', warped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()