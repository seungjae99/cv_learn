# 기울어진 종이 정렬시키기

import sys
import numpy as np
import cv2 as cv

def drawLines(img, ptrs):
    cpy = img.copy()
    color_p = (0, 0, 255)
    color_l = (255, 0, 0)
    
    for pt in ptrs:
        cv.circle(cpy, tuple(pt.astype(int)), 10, color_p, -1, cv.LINE_AA)
        cv.line(cpy, tuple(ptrs[0].astype(int)), tuple(ptrs[1].astype(int)), color_l, 2, cv.LINE_AA)
        
    cv.line(cpy, tuple(ptrs[1].astype(int)), tuple(ptrs[2].astype(int)), color_l, 2, cv.LINE_AA)
    cv.line(cpy, tuple(ptrs[2].astype(int)), tuple(ptrs[3].astype(int)), color_l, 2, cv.LINE_AA)
    cv.line(cpy, tuple(ptrs[3].astype(int)), tuple(ptrs[0].astype(int)), color_l, 2, cv.LINE_AA)
    
    return cpy

def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src
    
    if event == cv.EVENT_LBUTTONDOWN:
        for i in range(4):
            if cv.norm(srcQuad[i] - (x, y)) < 25:
                dragSrc[i] = True
                ptOld = (x, y)
                break
            
    if event == cv.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False
            
    if event == cv.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]:
                dx = x - ptOld[0]
                dy = y - ptOld[1]
                
                srcQuad[i] += (dx, dy)
                
                cpy = drawLines(src, srcQuad)
                cv.imshow('img', cpy)
                ptOld = (x, y)
                break
            
src = cv.imread('printed_document2.jpg')
src = cv.resize(src, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

if src is None:
    print('Image open failed!')
    sys.exit()
    
h, w = src.shape[:2]
dh = 500
dw = round(dh * 297 / 210)

srcQuad = np.array([[30, h - 30], [w - 30, h - 30], [w - 30, 30], [30, 30]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dragSrc = [False, False, False, False]

disp = drawLines(src, srcQuad)
cv.imshow('img', disp)
cv.setMouseCallback('img', onMouse)

while True:
    key = cv.waitKey()
    if key == 13:   # ENTER 키
        break
    elif key == 27: # ESC 키
        sys.exit()

pers = cv.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv.warpPerspective(src, pers, (dw, dh), flags=cv.INTER_CUBIC)

dst1 = cv.rotate(dst, cv.ROTATE_90_COUNTERCLOCKWISE)
# dst2 = cv.rotate(dst1, cv.ROTATE_180)

cv.imshow('Scanned Document', dst1)
cv.waitKey()
