# face detection

import cv2 as cv
import numpy as np

image = cv.imread('people.jpg')

cascade_face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
face_detections = cascade_face_detector.detectMultiScale(image, scaleFactor=1.05)

print(face_detections)

for (x, y, w, h) in face_detections:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
cv.imshow("face detection",image)
    
cv.waitKey(0)
cv.destroyAllWindows()
