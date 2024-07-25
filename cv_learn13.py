import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread("porsche1.png", cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("image file i`s not found")
    
histogram = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histogram, color='r', linewidth=1)
plt.show()

t, img_binary = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
cv.imshow('binary', img_binary)

histogram_b = cv.calcHist([img_binary], [0], None, [256], [0,256])
plt.plot(histogram_b, color='r', linewidth=1)
plt.show()