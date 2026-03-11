import cv2
import os

video = cv2.VideoCapture('video1.mp4')

try:
    if not os.path.exists('asset/video1.mp4'):
        os.makedirs('asset/video1.mp4')
except OSError:
    print('Error: Creating directory of data')
    
current_frame = 0
    
while(True):
    ret, frame = video.read()
    if ret:
        name = 'asset/video1.mp4/frame' + str(current_frame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        current_frame += 1
    else:
        break
video.release()
cv2.destroyAllWindows()
