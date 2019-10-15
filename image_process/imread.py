import cv2

img = cv2.imread('sample.jpg')

height, width, channels = img.shape
print(f'Image width = {width}, image height = {height}, channels = {channels}')

cv2.imshow("Image", img)
cv2.waitKey()