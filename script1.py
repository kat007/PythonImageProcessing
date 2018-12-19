import cv2

img = cv2.imread("galaxy.jpg")

print(type(img))
print(img)  #2D array

print(img.shape) #(1485, 990, 3)
print(img.ndim) #3

#resize_image = cv2.resize(img, (742, 445))
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(2000) #2 seconds
cv2.destroyAllWindows()

