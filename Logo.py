from moviepy import *
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def logo(videoFinal):
    output_path="C:/Edits_drama/outputvideo1.mp4"
    clip=VideoFileClip(videoFinal).subclip(20,30)
    text=TextClip("le bon spectacle",fontsize=30,color='white',bg_color='black',font='Bradley').set_position("right","bottom").set_duration(1)
    finalClip=CompositeVideoClip(clip,text)
    finalClip.write_videofile(output_path, fps=30, threads=1, codec="libx264")
logo("C:/Users/HP/Desktop/Love like the galaxy/Jodhaa Akbar (2008) @hindihdmovies.mkv")
