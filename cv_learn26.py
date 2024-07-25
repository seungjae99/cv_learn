# face + eye detection

import cv2 as cv
import numpy as np

image = cv.imread('people.jpg')

cascade_face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_eye_detector = cv.CascadeClassifier('haarcascade_eye.xml')

face_detections = cascade_face_detector.detectMultiScale(image,scaleFactor=1.03,
                                                         minNeighbors=6, minSize=(30,30))
eye_detections = cascade_eye_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=6,
                                                       minSize=(10, 10), maxSize=(30, 30))

# Draw face detection bounding-boxs 
for (x, y, w, h) in face_detections:
    cv.putText(image,'Faces',(x-5,y-5),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    
# Draw eye detection bounding-boxs 
for (x, y, w, h) in eye_detections:
    cv.putText(image,'Eyes',(x-5,y-5),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

cv.imshow("Eye Detection",image)

cv.waitKey(0)
cv.destroyAllWindows()
