import cv2 as cv
import sys

file_name = "sports_car"

img = cv.imread('porsche_cropped.png')

print(img.shape)
print(img[0,0,0], img[0,0,1], img[0,0,2])

if img is None:
    sys.exit('We cannot find images ~')

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
img_resized = cv.resize(img, dsize=(0,0), fx=2.0, fy=2.0, interpolation=cv.INTER_LINEAR)

cv.namedWindow('image')
cv.imshow('image', img) 
cv.imwrite('porsche.png', img)
cv.imwrite('porsche_gray.png', img_gray)
cv.imwrite('porsche_resized.png', img_resized)
cv.waitKey()

cv.destroyAllWindows()