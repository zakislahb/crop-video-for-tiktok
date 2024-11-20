from moviepy.video.io.VideoFileClip import VideoFileClip

def crop_video_to_9_8(input_path, output_path):
    """
    Crop the video to a 9:8 aspect ratio while keeping it centered.
    
    Args:
        input_path (str): Path to the input video.
        output_path (str): Path to save the cropped video.
    """
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Get the original video dimensions
    video_width, video_height = clip.size
    
    # Target aspect ratio
    target_aspect_ratio = 9 / 8
    
    # Calculate the target height and width
    if video_width / video_height > target_aspect_ratio:
        # Crop width to match the aspect ratio
        new_width = int(video_height * target_aspect_ratio)
        x1 = (video_width - new_width) // 2
        x2 = x1 + new_width
        cropped_clip = clip.crop(x1=x1, x2=x2)
    else:
        # Crop height to match the aspect ratio
        new_height = int(video_width / target_aspect_ratio)
        y1 = (video_height - new_height) // 2
        y2 = y1 + new_height
        cropped_clip = clip.crop(y1=y1, y2=y2)
    
    # Write the cropped video to the output path
    cropped_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    cropped_clip.close()
    clip.close()

# Example usage
input_video_path = "input_video.mp4"  # Replace with your video path
output_video_path = "output_video_9_8.mp4"  # Replace with your desired output path

crop_video_to_9_8(input_video_path, output_video_path)
