# Rotate image

import cv2 as cv
import numpy as np
import math

img = cv.imread('coin.png', cv.IMREAD_COLOR)

img90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
img180 = cv.rotate(img, cv.ROTATE_180)
img270 = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

#warpAffine 이용
h, w, c = img.shape
cp = (w//2, h//2) 
rot = cv.getRotationMatrix2D(cp, 20, 0.5)
# 이렇게도 표현이 가능하다.
# rad = 20 * math.pi /180
# rot = np.array([0.5 * math.cos(rad), math.sin(rad), 0],
#                [-math.cos(rad), 0.5 * math.cos(rad), 0],
#                dtype=np.float32)

img20 = cv.warpAffine(img, rot, (0,0))

cv.imshow('original', img)
cv.imshow('rotate20', img20)
cv.imshow('rotate90', img90)
cv.imshow('rotate180', img180)
cv.imshow('rotate270', img270)

cv.waitKey(0)
cv.destroyAllWindows()
