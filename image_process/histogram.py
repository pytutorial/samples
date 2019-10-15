import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sample.jpg')
pixels = img.reshape(-1, 3)

hist_r = [0] * 256
hist_g = [0] * 256
hist_b = [0] * 256

for (b, g, r) in pixels:
    hist_r[r] += 1
    hist_g[g] += 1
    hist_b[b] += 1
    
plt.plot(hist_r, 'r', label='red')
plt.plot(hist_g, 'g', label='green')
plt.plot(hist_b, 'b', label='blue')

plt.xlabel('Brightness')
plt.ylabel('Number of pixel')
plt.legend(loc='upper center')

plt.show()    