import cv2
import numpy as np
import imutils

altura = 300
largura = 300

original = True
cinza = False


cap = cv2.VideoCapture(0)

    
    
    

while True:
    ret, img_origial = cap.read()
    gray = cv2.cvtColor(img_origial, cv2.COLOR_BGR2GRAY)
    cv2.imshow('original',img_origial)
    cv2.imshow('Cinza',gray)
    key = cv2.waitKey(1)
    if key == 27:
        break
   
    