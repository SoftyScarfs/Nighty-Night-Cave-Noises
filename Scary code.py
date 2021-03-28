# imports
# pip install paysound
import playsound
import os
import random


# variables
# Find where the file is saved so it will run properly on any computer
cwd = os.getcwd()
print(cwd)



# light value detection


# play random sound sound
SndNum = random.randint(0,12)
playsound.playsound(str(cwd) + "\CaveSounds\CaveSnd" + str(SndNum) +".mp3")
