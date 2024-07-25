# hough transform(find coin)

import cv2 as cv

img = cv.imread("coin.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blr = cv.GaussianBlur(gray,(0,0),3)

circles=cv.HoughCircles(blr, cv.HOUGH_GRADIENT,1,20,
                        param1=50,param2=30,
                        minRadius=0,maxRadius=0)

for i in circles[0]:
    cv.circle(img, (int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)
    
cv.imshow("Circle detection", img)
cv.waitKey(0)
cv.destroyAllWindows()
