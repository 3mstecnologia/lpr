import pytesseract
import cv2

a = cv2.imread('1.jpg')
configtess = r' --oem 3 --psm 6'
text = pytesseract.image_to_string(a, config=configtess)
print(text)


