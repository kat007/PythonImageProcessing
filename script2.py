#Write a script that resizes all images in a directory to 100x100.
import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    print(image)
    img = cv2.imread(image, 0)
    resized_img = cv2.resize(img, (100, 100))
    cv2.imshow("image", resized_img)
    cv2.waitKey(2000)  # 2 seconds
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resized_img)
