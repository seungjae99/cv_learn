import cv2 as cv
import sys

def draw_rectangle(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 5, (0,0,255), -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), 5, (0,0,255), -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), 5, (255,0,0), -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), 5, (255,0,0), -1)
    cv.imshow("Draw3", img)

img = cv.imread("trump.jpg")
if img is None:
    sys.exit("image file is not found")
cv.imshow("Draw3", img)

cv.setMouseCallback("Draw3", draw_rectangle)

while(True):
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
