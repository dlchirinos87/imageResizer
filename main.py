import cv2
import glob

img_list = glob.glob("originalImages/*")
img_list.reverse()

a = 1
for img in img_list:
    image = cv2.imread(img, 1)
    width = 1000
    height = int(image.shape[0]*1000/image.shape[1])
    dims = (width, height)
    new_image = cv2.resize(image, dims)
    cv2.imwrite(f"resizedImages/resized_image{a}.jpg", new_image)
    a += 1
