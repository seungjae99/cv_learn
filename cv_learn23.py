# affine Transform 실습

import cv2 as cv
import numpy as np

img = cv.imread("iu.jpg")
img = cv.resize(img, dsize=(0,0), fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)

# 어파인 행렬 생성
aff = np.array([[1, 0.5, 0], [0, 1, 0]], dtype=np.float32)

h, w, c = img.shape

dst = cv.warpAffine(img, aff, (w + int(h * 0.5), h))

cv.imshow('Original Image', img)
cv.imshow('Affine Transform', dst)

cv.waitKey(0)
cv.destroyAllWindows()
