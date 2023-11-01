import os, subprocess, json

def check_files(stringu):
    for file in os.listdir(f'{rwd}\Output'):
        if stringu in file.split(os.sep)[-1]:
            return True
    return False

def make_a_video(file_name, fps, V_Type):
    global cone
    if check_files(V_Type):
        cone += 1
        # Get all image files in the working directory
        images = []
        for filename in os.listdir(f'{rwd}\Output'):
            if filename.startswith('image (') and filename.endswith(V_Type):
                images.append(os.path.join('Output', filename))

        # Sort the image files by their number
        images.sort(key=lambda x: int(x.split('(')[1].split(')')[0]))

        # Use ffmpeg to create the video
        subprocess.run(['ffmpeg', '-r', str(fps), '-i', f'{rwd}\Output\image (%d{V_Type}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f'{rwd}\{file_name}A-output-{cone}.mp4'])
        print('Video created successfully!')


# Get the frame rate from the text file
rwd = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
avd = os.path.join(rwd, 'A-VideoData.json')
with open(avd, "r") as infile:
    El_Data = json.load(infile)
    fn = El_Data["file_name"]
    fps = El_Data["fps"]

cone = 0
V_Types = [').png', ')-1.png', ')-2.png', ')-3.png', ')-0000.png', ')-0000-1.png', ')-0000-2.png', ')-0000-3.png']

for vt in V_Types:
    make_a_video(fn, fps, vt)
