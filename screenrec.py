import cv2
import numpy as np
import pyautogui
import pygetwindow
import logging

logging.basicConfig(format="%(levelname)s [%(asctime)s] %(message)s", level=logging.DEBUG)

gameWindow = pygetwindow.getWindowsWithTitle("SM-G900F")
if gameWindow == []:
    logging.error("scrcpy window not found")
    exit()
else:
    gameWindow = gameWindow[0]

topleft = gameWindow.topleft
bottomright = gameWindow.bottomright
w, h = bottomright.x - topleft.x, bottomright.y - topleft.y
w
print(topleft, w, h)

frameData = pyautogui.screenshot(region=(topleft.x, topleft.y, w, h))
frame = cv2.cvtColor(np.array(frameData), cv2.COLOR_RGB2BGR)

cv2.imshow("Screen", frame)
cv2.waitKey(0)

cv2.destroyAllWindows()
