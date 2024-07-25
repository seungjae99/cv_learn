# 자르기

import cv2 as cv
import sys

img = cv.imread("porsche_cropped.png")

if img is None:
    sys.exit("image file is not found")
    
h, w, c = img.shape

cv.imshow('origin image', img)
cv.imshow('image up left', img[:h//2,:w//2])

cv.waitKey(0)
cv.destroyAllWindows()