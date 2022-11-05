# Import library moviepy
from moviepy.editor import VideoFileClip

# User Input the name of the file
n = str(input("Enter name of the file with .mp4 extension: "))
# Performing transformstion
video = VideoFileClip(n)
# Saving the GIF file
video.write_gif(n +"_updated")

## The MP4 file muust be in the same folder as this code *****
