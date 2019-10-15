import cv2

img = cv2.imread('sample.jpg')
img2 = cv2.resize(img, (400, 400))
cv2.imwrite('output.jpg', img2)