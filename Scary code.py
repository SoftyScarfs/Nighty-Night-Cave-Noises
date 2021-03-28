# imports
# pip install paysound
import playsound
import os
import random
import PIL
from PIL import Image
import cv2, time

# variables
# Find where the file is saved so it will run properly on any computer
cwd = os.getcwd()


# light value detection

# video
video=cv2.VideoCapture(0)
check, frame = video.read()

filename = frame
# value detection
img = filename
print(frame)
colors = img.getpixel((320,240))
print(colors)
str(colors).split(", ")
value = int(colors[0]) + int(colors[1]) + int(colors[2])
value = value / 3
print(value)
# play random sound sound
SndNum = random.randint(0,12)
playsound.playsound(str(cwd) + "\CaveSounds\CaveSnd" + str(SndNum) +".mp3")
video.release()
