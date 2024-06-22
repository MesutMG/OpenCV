import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('videosample.mp4')

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
