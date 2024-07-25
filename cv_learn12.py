
import cv2 as cv
import numpy as np

img = cv.imread("iu.jpg")

img = cv.medianBlur(img, 5)
img = cv.GaussianBlur(img, (3, 3), 0)
img = cv.blur(img, (5,5))

sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5,-1],
                              [0, -1, 0]])

shapening_mask1 = np.array([[-1, -1, -1],
                            [-1, 9, -1],
                            [-1, -1, -1]])

smoothing_mask = np.array([[1/16, 1/8, 1/16],
                           [1/8, 1/4, 1/8],
                           [1/16, 1/8, 1/16]])

# 필터 적용
img2 = cv.filter2D(img, -1, sharpening_kernel)
img3 = cv.filter2D(img, -1, shapening_mask1)
img4 = cv.filter2D(img3, -1, smoothing_mask)

# cv.imshow("image1", img)
# cv.imshow("image2", img2)
# cv.imshow("image3", img3)
cv.imshow("image4", img4)


cv.waitKey(0)
cv.destroyAllWindows()