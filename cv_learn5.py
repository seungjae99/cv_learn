# 마우스 드래그로 도형크기 조절하기

import cv2 as cv
import sys

def draw_rectangle(event, x, y, flags, param):
    global ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x,y), (0,0,255), 2)
    cv.imshow('Draw2', img)
    
    
filename = "trump.jpg"
img = cv.imread(filename)

if img is None:
    sys.exit("we cannot find the image ~")
    
cv.imshow('Draw Test', img)
cv.setMouseCallback('Draw Test', draw_rectangle)

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break