from picamera2 import Picamera2
import cv2
import numpy as np

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

while True:

    frame = picam2.capture_array()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) > 500:

            x,y,w,h = cv2.boundingRect(contour)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break