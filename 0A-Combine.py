import os, subprocess, json

def check_files(numbero, stringu):
    for file in os.listdir(fr'{rwd}\Output-{numbero}'):
        if stringu in file.split(os.sep)[-1]:
            return True
    return False

def rename_files(directory):
    for filename in os.listdir(directory):
        if not filename.startswith("image") and filename.endswith(".png"):
            new_filename = filename[filename.index("image"):]
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

def make_a_video(file_number, file_name, fps, V_Type):
    global cone, rwd
    picklefile = fr'{rwd}\Output-{file_number}'
    if check_files(file_number, V_Type):
        rename_files(picklefile)
        cone += 1
        # Get all image files in the working directory
        images = []
        for filename in os.listdir(picklefile):
            if filename.startswith('image (') and filename.endswith(V_Type):
                images.append(os.path.join(picklefile, filename))

        # Sort the image files by their number
        images.sort(key=lambda x: int(x.split('(')[1].split(')')[0]))

        # Use ffmpeg to create the video
        subprocess.run(['ffmpeg', '-r', str(fps), '-i', fr'{rwd}\Output-{file_number}\image (%d{V_Type}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', fr'{rwd}\{file_name}A-output-{cone}.mp4'])
        print('Video created successfully!')


# Start the program. Ask the user which folder to combine
while True:
    try:
        user_input = input("Enter the number of the Output folder to combine: ")
        El_F = int(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
# Get the frame rate from the text file
rwd = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
avd = os.path.join(fr'{rwd}\Output-{El_F}', f'.VideoData.json')
with open(avd, "r") as infile:
    El_Data = json.load(infile)
    fn = El_Data["file_name"]
    fps = El_Data["fps"]

cone = 0
V_Types = [').png', ')-1.png', ')-2.png', ')-3.png', ')-0000.png', ')-0000-1.png', ')-0000-2.png', ')-0000-3.png']

for vt in V_Types:
    make_a_video(El_F, fn, fps, vt)
