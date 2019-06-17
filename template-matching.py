import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cropTemplate = cv2.imread("characterHead.png", 0)
    w, h = cropTemplate.shape[::-1]

    res = cv2.matchTemplate(imgGray, cropTemplate, cv2.TM_CCOEFF_NORMED)
    threshhold = 0.7
    detections = np.where(res >= threshhold)

    for pt in zip(*detections[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,255),2)

    cv2.imshow("Main", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
