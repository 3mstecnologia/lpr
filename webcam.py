import cv2

from openalpr import Alpr

alpr = Alpr("br", "openalpr.conf", "runtime_data")

if not alpr.is_loaded():
     print("Error loading OpenALPR")
     sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    img_str = cv2.imencode('.jpg', img)[1].tostring()

    results = alpr.recognize_array(img_str)

    for plate in results['results']:
        cv2.putText(img, plate['plate'], (plate['coordinates'][0]['x'], plate['coordinates'][0]['y']-5), 0, 1, (255,0,0), 3 )
        cv2.rectangle(img,(plate['coordinates'][0]['x'], plate['coordinates'][0]['y']), (plate['coordinates'][2]['x'], plate['coordinates'][2]['y']), (255,0,0), 3)



    cv2.imshow('img', img)

    key = cv2.waitKey(1)

    if key == 27:
        break
