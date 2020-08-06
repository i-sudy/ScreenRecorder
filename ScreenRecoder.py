#Sudeep Dalela Screen Recorder

import cv2
import numpy as np
import pyautogui
from datetime import datetime

screen_size=(2880,1800)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("ScreenRecordedAt_"+datetime.now().strftime("%Y-%m-%d %H:%M:%S") +".avi",fourcc,20.0,(screen_size))



while True:
    # capture screen shots
    img=pyautogui.screenshot()
    # convert image in np array of image
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("show",frame)
    if cv2.waitKey(1)==ord("q"):
        break

