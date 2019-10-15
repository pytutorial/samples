import cv2

img = cv2.imread('sample.jpg')

img2 = img[150:-150,200:-200]
cv2.imwrite('output.jpg', img2)