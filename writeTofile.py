import os
import  cv2
import numpy as np

# Get the list of all files and directories
path = "C:/Users/HP/Desktop/Love like the galaxy"
dir_list = os.listdir(path)



# importing vlc module
import vlc

# importing time module
import time


# creating vlc media player object
media_player = vlc.MediaPlayer()

# media object
media = vlc.Media("C:/Users/HP/Desktop/Love like the galaxy/"+dir_list[0])

# setting media to the media player
media_player.set_media(media)


# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep()

# pausing media
media_player.set_pause(1)

# wait for 4 second
# so that it remained paused for 4 seconds
time.sleep()


# getting current media time
value = media_player.get_time()

# printing value
print("Current Media time : ")
print(value)
