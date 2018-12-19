# face detection
# face training samples are provided
# other training data can be found at:
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

#img = cv2.imread("photo.png")
img = cv2.imread("alice3.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)
# print(type(faces)) #<class 'numpy.ndarray'>
# print(faces)  #[[103 116 410 410]]
# The output values are the X Y coordinates (from the top-left corner),
# followed by width and height.


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))


cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()




