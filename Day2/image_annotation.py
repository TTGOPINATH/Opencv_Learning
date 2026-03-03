import cv2
import numpy as np

img = cv2.imread('wallpaper.jpg')

# image annotation using line
point_A = (500, 200)
point_B = (800, 200)
cv2.line(img,point_A,point_B,(100,250,0),thickness=2)
cv2.imshow('lined_image',img)
cv2.waitKey(0)
# image annotation using rectangle
top_left = (500, 300)
bottom_right = (800, 500)
cv2.rectangle(img,top_left,bottom_right,(0,255,0),thickness=2)
cv2.imshow('rectangled_image',img)
cv2.waitKey(0)
# image annotation using circle
center = (650, 400)
radius = 50
cv2.circle(img,center,radius,(255,0,0),thickness=2)
cv2.imshow('circled_image',img)
cv2.waitKey(0)

# image annotation using text
text_position = (500, 550)
cv2.putText(img,'Wallpaper',text_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),thickness=2)
cv2.imshow('text_image',img)
cv2.imwrite('annotated_image.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()