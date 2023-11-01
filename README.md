# A-Split-Combine
Split .mp4 videos into frames and combine frames into videos

Welcome! Here are two programs I breifly made to make life easier for making reanimations with Stable Diffusion.

Simply put the .py or .exe files in the directory where you want to manage your video creation.

How to use:
  Split: Run A-Split and drag a .mp4 video file into the terminal window. It will write the video file's path for you, then press enter.
    The splitter will create a data file with the video's fps and name in it. That'll be used in the A-Combine.
    Then it will create your Source and Output folders for you, and fill Source with the frames split from the provided video.

  Combine: Run A-Combine and it will automatically find the various image sets in the Output folder and combine them based on the fps in the datafile. It will name the new output videos based on the source video so they will be easy to find.

How to use with Stable Diffusion:
  After splitting a video file into frames, simply copy the Source folder path and put it into your Stable Diffusions batch input path.
  Then do the same with the Output folder.
  Now generate your images.
  When done, simply combine and enjoy your completed video.
