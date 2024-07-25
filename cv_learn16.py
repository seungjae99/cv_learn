import cv2 as cv
import numpy as np

gray = cv.imread("porsche1.png", cv.IMREAD_GRAYSCALE)
gray = cv.resize(gray, dsize=(0,0), fx=0.4, fy=0.4, interpolation=cv.INTER_AREA)

grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)

sobel_x=cv.convertScaleAbs(grad_x)
sobel_y=cv.convertScaleAbs(grad_y)

edge_strength=cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

results = np.hstack([gray, sobel_x, sobel_y])
cv.imshow("Sobel Edge Detection",results)

cv.waitKey(0)
cv.destroyAllWindows()