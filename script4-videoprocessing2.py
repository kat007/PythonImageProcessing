import cv2
import time


video = cv2.VideoCapture(0)  # my camera: 0

check, frame = video.read()

'''
print(type(check)) #<class 'bool'>
print(type(frame)) #<class 'numpy.ndarray'>

print(check)  #True
print(frame)  #[[[ 9 28  8]
               # [11 29  9]
               # [15 28 11]
               # ...
'''





gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
time.sleep(5)
cv2.imshow("VideoCapture", gray)



# pass zero to allow any buttn press to close the window
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()


