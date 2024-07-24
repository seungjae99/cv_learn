import cv2 as cv
import numpy as np
import sys

cap = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)

if not cap.isOpened():
    sys.exit("Camera Connected Failed")

frames = []

while(True):
    ret, frame = cap.read()
    
    if not ret:
        print("Frame acquation Failed~")
        break
    
    cv.imshow("Video display", frame)
    
    key = cv.waitKey(1)
    
    if key==ord('q'):
        break
    elif key==ord('c'):
        frames.append(frame)

cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    images = frames[0]
    for i in range(1, min(3, len(frames))):
        images = np.hstack((images, frames[i]))
    cv.imshow('Captured Images', images)
    
    cv.waitKey()
    cv.destroyAllWindows