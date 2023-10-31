import os
import subprocess

# Get the frame rate from the text file
with open('A-fps.txt', 'r') as f:
    fps = float(f.read())

# Get all image files in the working directory
images = []
for filename in os.listdir('.'):
    if filename.startswith('image (') and (filename.endswith(').png') or filename.endswith(')-0000.png')):
        images.append(filename)

# Sort the image files by their number
images.sort(key=lambda x: int(x.split('(')[1].split(')')[0]))

# Use ffmpeg to create the video
subprocess.run(['ffmpeg', '-framerate', str(fps), '-i', 'image (%d).png', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', 'A-output.mp4'])
print('Video created successfully!')
