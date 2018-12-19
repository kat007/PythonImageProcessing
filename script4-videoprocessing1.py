import cv2
import time

# shorter version
# import cv2, time


video = cv2.VideoCapture(0)  # my camera: 0
#video = cv2.VideoCapture("movie.mp4") # video file directory


#hold the video camera for 5 seconds
time.sleep(5)

#make sure camera is released

video.release()


