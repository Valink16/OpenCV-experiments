import cv2
from time import sleep

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

i = 1
while True:
    _, frame = cam.read()
    cv2.imwrite("shots/"+str(i)+".png", frame)
    sleep(2)
    i += 2

    cv2.imshow("Shot", frame)

    if cv2.waitKeyEx(10) & 0xFF == ord('q'):
        break

cam.release()
