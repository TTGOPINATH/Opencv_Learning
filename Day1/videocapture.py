


import cv2
import numpy as np
video = cv2.VideoCapture(0)   # 0 for webcam, 1 for external camera, and 'filename' for video file
if(video.isOpened()):
    FPS = video.get(cv2.CAP_PROP_FPS)
    Frame_rate = video.get(cv2.CAP_PROP_FRAME_COUNT)
    Frame_width = int (video.get(cv2.CAP_PROP_FRAME_WIDTH))
    Frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('Frames per second : ', FPS, 'FPS')
    print('Frame count : ', Frame_rate)
    print('Frame width : ', Frame_width, 'pixels')
    print('Frame height : ', Frame_height, 'pixels')
    frame_size = (Frame_width, Frame_height)
    
    video_out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, frame_size)
    while video.isOpened():
        ret,fps = video.read()
        if ret == True:
            video_out.write(fps)
            cv2.imshow('Video', fps)
            key = cv2.waitKey(20)
            if key == ord('q'):
                break
        else:
            break
video.release()
video_out.release()