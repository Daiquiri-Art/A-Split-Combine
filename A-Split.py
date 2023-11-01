import os, subprocess, json

def get_file_name(file_path: str) -> str:
    file_name = os.path.basename(file_path)
    return os.path.splitext(file_name)[0]

def split_video_into_frames(video_path):
    # Get the frame rate of the video
    cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
    fps = eval(subprocess.check_output(cmd, shell=True).decode().strip())

    # Create the source and output directories if they don't exist
    rwd = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    source_dir_path = os.path.join(rwd, 'Source')
    output_dir_path = os.path.join(rwd, 'Output')
    if not os.path.exists(source_dir_path):
        os.makedirs(source_dir_path)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    
    # Write a json for remaking the video from the new frames.
    avd = os.path.join(rwd, 'A-VideoData.json')
    fn = get_file_name(video_path)
    El_Data = {
        "file_name": fn,
        "fps": fps
    }
    with open(avd, "w") as outfile:
        json.dump(El_Data, outfile)

    # Split the video into frames
    cmd = f'ffmpeg -i "{video_path}" -vf fps={fps} "Source\image (%d).png"'
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    # Get the path of the video file
    video_path = input('Drag and drop the video file here: ').strip('"')

    # Split the video into frames
    split_video_into_frames(video_path)
