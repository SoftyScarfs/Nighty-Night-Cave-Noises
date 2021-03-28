# imports

# pip install paysound
import playsound
import random
import cv2
# pip install opencv-contrib-python
import numpy as np
import os
import time

# variables / def

def rescaleFrame(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
# Find where the file is saved so it will run properly on any computer
cwd = os.getcwd()


# light value detection

# get image
while True:
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    frameRes = rescaleFrame(frame)
    gray = cv2.cvtColor(frameRes, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        capture.release()
    cv2.destroyAllWindows()
    # When everything done, release the capture
    cap.release()
    # value detect historgram thing I think
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256] )
    print(int(gray_hist[140]))
    if int(gray_hist[140]) < int(150):
        # play random sound sound
        SndNum = random.randint(0,12)
        playsound.playsound(str(cwd) + "\CaveSounds\CaveSnd" + str(SndNum) +".mp3")
        time.sleep(60)
time.sleep(7)
