import cv2

img1 = cv2.imread("jet.png")
img2 = cv2.imread("python-logo.jpg")

r2, c2, ch2 = img2.shape
roi = img1[0:r2, 0:c2]

imgGray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(imgGray, 20, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

img1_res = cv2.bitwise_and(roi, roi, mask=maskInv)
img2_res = cv2.bitwise_and(img2, img2, mask=mask)

res = cv2.add(img1_res, img2)

img1[0:r2, 0:c2] = res


cv2.imshow("Final resut;", img1)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
