# face detection with camera

import cv2 as cv
import sys


def detect_faces(image):
    face_detections = cascade_face_detector.detectMultiScale(image,scaleFactor=1.03,
                                                             minNeighbors=6, minSize=(30,30))
    eye_detections = cascade_eye_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=6,
                                                           minSize=(10, 10), maxSize=(30, 30))

    # Draw face detection bounding-boxs 
    for (x, y, w, h) in face_detections:
        cv.putText(image,'Faces',(x-5,y-5),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    # Draw eye detection bounding-boxs 
    for (x, y, w, h) in eye_detections:
        cv.putText(image,'Eyes',(x-5,y-5),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return image

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
if not cap.isOpened():
    sys.exit("Camera Connection Failed")

cascade_face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_eye_detector = cv.CascadeClassifier('haarcascade_eye.xml')

frames = []
while(True):
    ret, frame = cap.read()
    if not ret:
        print("Frame acquation Failed~")
        break
        
    frame = detect_faces(frame)
    cv.imshow('Face Detection', frame)
    
    key = cv.waitKey(1)
    if key==ord('q'):
        break
    
cv.waitKey(0)
cv.destroyAllWindows()
