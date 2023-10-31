import os
import subprocess

def split_video_into_frames(video_path):
    # Get the frame rate of the video
    cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
    fps = eval(subprocess.check_output(cmd, shell=True).decode().strip())

    # Get the path of the parent directory of the current working directory
    parent_dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    
    # Create the output directory if it doesn't exist
    output_dir_path = os.path.join(parent_dir_path, 'Output')
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    # Create the file path
    file_path = os.path.join(output_dir_path, 'A-fps.txt')
    
    # Write to the file
    #open(file_path, 'w').close()
    with open(file_path, 'w') as f:
        f.write(str(fps))

    # Split the video into frames
    cmd = f'ffmpeg -i "{video_path}" -vf fps={fps} "image (%d).png"'
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    # Get the path of the video file
    video_path = input('Drag and drop the video file here: ').strip('"')

    # Split the video into frames
    split_video_into_frames(video_path)
