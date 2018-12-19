import cv2
import time


video = cv2.VideoCapture(0)  # my camera: 0

# count number of frames generated in the loop
a = 1

while True:
    a = a + 1

    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(5)
    cv2.imshow("VideoCapture", gray)

    #change wait time from 2000 to 1000 to 1
    # if wait key is zero, zero means q
    key = cv2.waitKey(1)

    #press on Q button on keyboard, break the loop
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print(a)


