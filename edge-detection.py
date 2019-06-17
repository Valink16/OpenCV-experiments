import cv2

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    cv2.imshow("Camera source", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("sobelx", sobelx)
    cv2.imshow("sobely", sobely)

    if cv2.waitKey(15) & 0xFF == ord ('q'):
        break
