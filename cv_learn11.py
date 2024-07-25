# blur
import cv2 as cv

img = cv.imread("porsche1.png")

img_median_blur = cv.medianBlur(img, 3)

cv.imshow("original image", img)
cv.imshow("denoised image", img_median_blur)

cv.waitKey(0)
cv.destroyAllWindows()