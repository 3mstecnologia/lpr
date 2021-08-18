import cv2
import numpy as np
import imutils



altura = 300
largura = 300

original = False
cinza = False
filtrada = False
bordas = False
imagemcontornada = True
imagemtopcontornos = True
placadetectada = True


cameraPatio = 'rtsp://admin:admin@192.168.88.100:554/cam/realmonitor?channel=2&subtype=0'
camerafrontal1 = 'rtsp://admin:admin@192.168.88.100:554/cam/realmonitor?channel=1&subtype=0'
camerafrontal2 = 'rtsp://admin:admin@192.168.88.100:554/cam/realmonitor?channel=3&subtype=0'

cap = cv2.VideoCapture(0)

    
    
    

while True:
    ret, img_origial = cap.read()
    gray = cv2.cvtColor(img_origial, cv2.COLOR_BGR2GRAY)
    if original == True:
        cv2.imshow('original',img_origial)
    if cinza == True:
        cv2.imshow('Cinza',gray)
    gray = cv2.bilateralFilter(gray, 11,17,17)
    if filtrada == True:
        cv2.imshow('Filtrada', gray)
    bordas1 = cv2.Canny(gray, 170, 200)
    if bordas == True:
        cv2.imshow('Bordas', bordas1)
    contornos, _  = cv2.findContours(bordas1.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    imagem_desenhada = img_origial.copy()
    cv2.drawContours(imagem_desenhada, contornos, -1, (0,255,0), 3)
    if imagemcontornada == True:
        cv2.imshow('Contornos', imagem_desenhada)
    contornos = sorted(contornos, key = cv2.contourArea, reverse = True)[:30]
    NumPlacaCnt = None

    imagem_topcontornos = img_origial.copy()
    cv2.drawContours(imagem_topcontornos, contornos, -1, (0,255,0),3)
    if imagemtopcontornos == True:
        cv2.imshow('Contornos', imagem_topcontornos)


    count = 0
    idx = 1
    NumPlacaCnt = []
    for c in contornos:
        perimetr = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02*perimetr, True)
        if len(approx) == 4:
            NumPlacaCnt = approx

            x,y,w,h = cv2.boundingRect(c)
            nova_imagem = gray[y:y+h, x:x+w]
            cv2.imwrite('Placa' + str(idx)+ '.png', nova_imagem)
            break
    if len(NumPlacaCnt) != 0:
        cv2.drawContours(img_origial, [NumPlacaCnt], -1,(0,255,0), 3)
    if placadetectada == True:
        cv2.imshow('Placa Detectada', nova_imagem)



    




    key = cv2.waitKey(1)
    if key == 27:
        break
   
    