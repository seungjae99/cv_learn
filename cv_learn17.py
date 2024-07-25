import cv2 as cv
import numpy as np

gray = cv.imread("trump.jpg", cv.IMREAD_GRAYSCALE)
gray = cv.resize(gray, dsize=(0,0), fx=0.7, fy=0.7, interpolation=cv.INTER_AREA)

canny1=cv.Canny(gray,50,150)
canny2=cv.Canny(gray,100,200)

results = np.hstack([gray, canny1, canny2])
cv.imshow("Canny Edge Detection",results)

cv.waitKey(0)
cv.destroyAllWindows()
