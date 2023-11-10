import os, subprocess, json

def get_file_name(file_path: str) -> str:
    file_name = os.path.basename(file_path)
    return os.path.splitext(file_name)[0]

def is_directory_empty(directory_path: str) -> bool:
    if not os.path.exists(directory_path):
        return True
    return len(os.listdir(directory_path)) == 0

def split_video_into_frames(video_path):
    # Get the frame rate of the video
    cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
    fps = eval(subprocess.check_output(cmd, shell=True).decode().strip())
    fn = get_file_name(video_path)

    # Create the source, output, and video data directories if they don't exist
    rwd = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    
    Vi = 0
    while True:
        source_dir_path = os.path.join(rwd, f'Source-{Vi}')
        output_dir_path = os.path.join(rwd, f'Output-{Vi}')
        if is_directory_empty(source_dir_path):
            os.makedirs(source_dir_path)
            if not os.path.exists(output_dir_path):
                os.makedirs(output_dir_path)
            break
        Vi += 1


    # Write a json for remaking the video from the new frames
    avd = os.path.join(output_dir_path, f'.VideoData.json')
    El_Data = {
        "file_name": fn,
        "fps": fps
    }
    with open(avd, "w") as outfile:
        json.dump(El_Data, outfile)

    # Split the video into frames
    cmd = fr'ffmpeg -i "{video_path}" -vf fps={fps} "Source-{Vi}\image (%d).png"'
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    # Get the path of the video file
    video_path = input("""
                       A-Split
                       By Daiquiri

                       Drag and drop the video file into the terminal here and press enter:
    """).strip('"')

    # Split the video into frames
    split_video_into_frames(video_path)
