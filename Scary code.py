# imports
import playsound
import os
import random


# variables
cwd = os.getcwd()
print(cwd)
SndNum = random.randint(0,4)


# light value detection


# play random sound sound
playsound.playsound(str(cwd) + "\CaveSounds\CaveSnd" + str(SndNum) +".mp3")
