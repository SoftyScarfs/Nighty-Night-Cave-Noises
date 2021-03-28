# imports

# pip install paysound
import playsound
import random

# variables

# Find where the file is saved so it will run properly on any computer
cwd = os.getcwd()



# light value detection

# get image

# value detect



# play random sound sound
SndNum = random.randint(0,12)
playsound.playsound(str(cwd) + "\CaveSounds\CaveSnd" + str(SndNum) +".mp3")
video.release()
