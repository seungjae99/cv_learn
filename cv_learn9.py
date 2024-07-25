import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread("gamma_ex_resized.jpg")
if img is None:
    sys.exit("image file not found")
cv.imshow("original image", img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("gray image", gray)

stretch = cv.normalize(gray,None,0,255, cv.NORM_MINMAX)
cv.imshow("stretched image", stretch)

equal = cv.equalizeHist(gray)
cv.imshow("Equalized image", equal)

equal_b = cv.equalizeHist(img[:,:, 0])
equal_g = cv.equalizeHist(img[:,:,1])
equal_r = cv.equalizeHist(img[:,:,2])
equal_color = cv.merge([equal_b, equal_g, equal_r])
cv.imshow("equalized color image", equal_color)

cv.waitKey()
cv.destroyAllWindows()