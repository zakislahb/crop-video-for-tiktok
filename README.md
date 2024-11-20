# crop-video-for-tiktok
This is a Python application that crops any video to a 9:8 format while keeping it centered, you can use the `moviepy` library.

### Requirements

Install the required library using pip:

`pip install moviepy`

### Explanation

1.  **Load the Video**: The `VideoFileClip` function loads the input video.
2.  **Aspect Ratio**: The target aspect ratio is `9:8`. The script calculates whether the width or height needs cropping to achieve this ratio.
3.  **Crop**: The `crop` method in `moviepy` is used to center the crop by calculating the offsets.
4.  **Save the Video**: The `write_videofile` method saves the cropped video to the specified path.

### Usage

Replace `input_video.mp4` with your video file path and `output_video_9_8.mp4` with the desired output path. Run the script, and your video will be cropped to the `9:8` format.

If you encounter any issues or need further assistance, feel free to ask!
