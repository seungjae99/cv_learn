# 마우스 입력으로 왼쪽클릭하면 laugh, 오른쪽클릭하면 crying 출력하기

import cv2 as cv
import sys

def draw_rectangle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+100, y+100), (0,0,255), 2)
        cv.putText(img, 'laugh', (x,y-2), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x,y), (x+100, y+100), (255,0,0), 2)
        cv.putText(img, 'crying', (x,y-2), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)
    cv.imshow('Draw Test', img)
    
    
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