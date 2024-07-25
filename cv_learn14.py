import cv2 as cv
import sys
import numpy as np

img = cv.imread("coin.png", cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("image file is not found!")
# cv.imshow('original', img)

se = np.uint8([[1,1,1],
               [1,1,1],
               [1,1,1]])

se2 = np.uint8([[0,1,0],
               [1,1,1],
               [0,1,0]])

se3 = np.uint8([[0,0,1,0,0],
               [0,1,1,1,0],
               [1,1,1,1,1],
               [0,1,1,1,0],
               [0,0,1,0,0]])


se4 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (128, 128))

t, img_binary = cv.threshold(img,100,255,cv.THRESH_BINARY)
# cv.imshow('binary', img_binary)



# opened_img = cv.morphologyEx(img_binary,cv.MORPH_OPEN, se)
# cv.imshow("opened image",opened_img)

closed_image = cv.morphologyEx(img_binary,cv.MORPH_CLOSE, se)
# cv.imshow("closed image",closed_image)

dilated_img = cv.dilate(closed_image,se,iterations=1)
# cv.imshow("dilated image", dilated_img)

eroded_img = cv.erode(dilated_img,se2,iterations=1)
cv.imshow("eroded image1", eroded_img)

eroded_img2 = cv.erode(dilated_img,se3,iterations=1)
cv.imshow("eroded image2", eroded_img)

eroded_img3 = cv.erode(dilated_img,se4,iterations=1)
cv.imshow("eroded image3", eroded_img)


cv.waitKey(0)
cv.destroyAllWindows()

