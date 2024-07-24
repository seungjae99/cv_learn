# 이미지에 사각형이랑 텍스트 그려넣기

import cv2 as cv
import sys

filename = "trump.jpg"
img = cv.imread(filename)

if img is None:
    sys.exit("we cannot find the image ~")
   
print(img.shape) 
cv.rectangle(img, (320, 180), (400, 260), (0,0,255), 2)
cv.putText(img, 'fight', (320, 280), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),1)

cv.imshow("Draw Test", img)

cv.waitKey()
cv.destroyAllWindows