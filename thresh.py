import cv2

img = cv2.imread("jet2.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(imgGray, 200, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

cv2.imshow("Main", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("mask", mask)
cv2.imshow("maskInv", maskInv)

cv2.waitKey(0)
cv2.destroyAllWindows()
