# blur
import cv2 as cv

img = cv.imread("porsche_cropped.png")
img_resized = cv.resize(img, dsize=(0,0), fx=0.7, fy=0.7, interpolation=cv.INTER_AREA)
cv.imwrite('porsche1.png', img_resized)
img = cv.imread("porsche1.png")

img_blur3 = cv.blur(img, (3,3))
img_blur33 = cv.blur(img, (33,33))

cv.imshow("original image", img)
cv.imshow("blur-3 image", img_blur3)
cv.imshow("blur-33 image", img_blur33)

cv.waitKey(0)
cv.destroyAllWindows()