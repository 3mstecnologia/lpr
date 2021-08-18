import cv2
import numpy as np
import imutils

altura = 300
largura = 300

original = True
cinza = False


cap = cv2.VideoCapture(0)

    
    
    

if original == True:
    while True:
        
        ret, img_origial = cap.read()
        cv2.imshow('original',img_origial)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        break
   
    