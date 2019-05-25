import pyautogui
import cv2
import numpy as np
import socket
import datetime

def takescreenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    name =  "screen_{0}_{1}.png".format(socket.gethostname(), datetime.datetime.now().date()) 
    cv2.imwrite(name, image)
    return name