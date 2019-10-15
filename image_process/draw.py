import cv2
import numpy as np

RED = (0, 0, 255)
GREEN = (0, 255, 0)

width = 640
height = 480
channels = 3

img = 255 * np.ones((height, width, 3), dtype='uint8')

cv2.rectangle(img, (100, 100), (200, 200), RED, 2)

cv2.circle(img , (300, 300), 50, GREEN, -1)

cv2.imwrite('output.jpg', img)