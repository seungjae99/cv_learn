# 감마 보정

import cv2 as cv
import numpy as np

def gamma(f, gamma=1.0):
    f1 = f/255.0
    return np.uint8(255*(f1**gamma))

img = cv.imread("gamma_ex.jpg")
img_resized = cv.resize(img, dsize=(0,0), fx=0.3, fy=0.3, interpolation=cv.INTER_LINEAR)
cv.imwrite('gamma_ex_resized.jpg', img_resized)
img = cv.imread("gamma_ex_resized.jpg")

images = [gamma(img, 0.4), gamma(img, 0.5), gamma(img, 0.7),
          gamma(img, 0.9), gamma(img, 1.2), gamma(img, 2.0)]

row1 = np.hstack(images[:3])
row2 = np.hstack(images[3:])

gammas = np.vstack([row1, row2])

cv.imshow('gammas', gammas)
cv.waitKey(0)
cv.destroyAllWindows()

