# import time
import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt
import time
# import mediapipe as mp
# import tensorflow as tf
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# Set mediapipe model 
t =0
# while cap.isOpened():
while True:
    t = time.time()
        # Read feed
    ret, frame = cap.read()



        # Show to screen
    cv2.imshow('OpenCV Feed', frame)
    print('fps', 1/(time.time()-t))
        # Break gracefully

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()