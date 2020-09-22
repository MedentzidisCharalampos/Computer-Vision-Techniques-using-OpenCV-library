import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur= cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
lap = np.uint8(np.absolute(lap))
sobel1X = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel1Y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel1X = np.uint8(np.absolute(sobel1X))
sobel1Y = np.uint8(np.absolute(sobel1Y))
sobelCombined = cv2.bitwise_or(sobel1X, sobel1X)
canny = cv2.Canny(img, 100, 200)

titles = ['image', '2d Convolution', 'blur', 'GaussianBlur', 'median', 'bilateral', 'laplacian', 'sobel1x', 'sobel1y', 'sobelCombined', 'Canny']
images = [img, dst, blur, gblur, median, bilateralFilter, lap, sobel1X, sobel1Y, sobelCombined, canny]

for i in range(11):
    plt.subplot(6, 5, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()