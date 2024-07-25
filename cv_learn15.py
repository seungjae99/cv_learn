import cv2 as cv
import numpy as np

img = cv.imread("iu.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.resize(gray, dsize=(0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)

blurring_mask1 = np.full((3, 3), 1/9)

blurring_mask2 = np.full((5,5), 1/25)

smoothing_mask = np.array([[1/16, 1/8, 1/16],
                           [1/8, 1/4, 1/8],
                           [1/16, 1/8, 1/16]])

shapening_mask1 = np.array([[-1, -1, -1],
                            [-1, 9, -1],
                            [-1, -1, -1]])

shapening_mask2 = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

blurring1 = cv.filter2D(gray, -1, blurring_mask1)
blurring2 = cv.filter2D(gray, -1, blurring_mask2)

smoothing = cv.filter2D(gray, -1, smoothing_mask)

sharpening1 = cv.filter2D(gray, -1, shapening_mask1)
sharpening2 = cv.filter2D(gray, -1, shapening_mask2)

images = np.hstack([blurring1, blurring2,
                    smoothing,
                    sharpening1, sharpening2])

cv.imshow('blurring1', images)

cv.waitKey(0)
cv.destroyAllWindows()