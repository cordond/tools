from moviepy.editor import *

def merge_videos_side_by_side(video_paths, output_path):
    '''
    Merges multiple videos side by side into a single video.
    Inputs:
        video_paths: a list of paths to the videos to be merged
        output_path: the path to the output video
    Example usage:
        video_paths = ["video1.mp4", "video2.mp4", "video3.mp4"]
        merge_videos_side_by_side(video_paths, "output.mp4")
    '''
    # Load video clips
    clips = [VideoFileClip(video_path) for video_path in video_paths]

    # Resize videos to have the same height
    min_height = min(clip.h for clip in clips)
    clips = [clip.resize(height=min_height) for clip in clips]

    # Create a side-by-side layout
    final_clip = clips_array([clips])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

    # Close video clips
    for clip in clips:
        clip.close()

def merge_videos_vertically(video_paths, output_path):
    '''
    Merges multiple videos vertically into a single video.
    Inputs:
        video_paths: a list of paths to the videos to be merged
        output_path: the path to the output video
    Example usage:
        video_paths = ["video1.mp4", "video2.mp4", "video3.mp4"]
        merge_videos_vertically(video_paths, "output.mp4")
    '''
    # Load video clips
    clips = [VideoFileClip(video_path) for video_path in video_paths]

    # Resize videos to have the same height
    min_height = min(clip.h for clip in clips)
    clips = [clip.resize(height=min_height) for clip in clips]

    # Create a side-by-side layout
    final_clip = clips_array([[clip] for clip in clips])

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

    # Close video clips
    for clip in clips:
        clip.close()

def add_text_to_video(video_path, text_elements, output_path):
    '''
    Adds text to a video.
    Inputs:
        video_path: the path to the video
        text_elements: a list of dictionaries, each containing the text to be added and its position
            text: the text to be added
            relative_position: the position of the text, a tuple of relative coordinates (relative to left and top)
            fontsize: the fontsize of the text
            color: the color of the text
            font: the font of the text
        output_path: the path to the output video
    Example usage:
        video_path = "video.mp4"
        text_elements = [{"text": "Hello", "relative_position": (0.5, 0.5)}, 
                         {"text": "World", "relative_position": (0.5, 0.4)}]
        add_text_to_video(video_path, text_elements, "output.mp4")
    '''
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Create a list to hold TextClip objects
    text_clips = []

    # Create TextClip objects for each text element
    for text_info in text_elements:
        text = text_info['text']
        fontsize = text_info.get('fontsize', 50)
        color = text_info.get('color', 'white')
        position = text_info.get('relative_position', ('0.5', '0.8'))
        font = text_info.get('font', 'Helvetica-Light')

        text_clip = TextClip(text, fontsize=fontsize, color=color, font=font)
        text_clip = text_clip.set_pos((position), relative=True).set_duration(video_clip.duration)

        text_clips.append(text_clip)

    # Composite the video clip and the text clips
    final_clip = CompositeVideoClip([video_clip] + text_clips)

    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264", fps=24)

    # Close video clips
    video_clip.close()
    final_clip.close()

    pass

# Example usage with multiple videos
# video_paths_merge = ["/Users/cordond/Desktop/mx.mov", "/Users/cordond/Desktop/my.mov", "/Users/cordond/Desktop/mz.mov"]
# merge_videos_side_by_side(video_paths_merge, "/Users/cordond/Desktop/output_m.mp4")

# video_path = "/Users/cordond/Desktop/output_m.mp4"
# column_width = 1/3
# text_elements = [{"text": "mx: 0.1", "relative_position": (column_width/2, 0.80)}, 
#                  {"text": "my: 0.1", "relative_position": (0.5, 0.80)},
#                  {"text": "mz: 0.1", "relative_position": (1-column_width/2, 0.80)}]
# add_text_to_video(video_path, text_elements, "/Users/cordond/Desktop/output_m_text.mp4")

video_paths_merge = ["/Users/cordond/Desktop/output_text.mp4", "/Users/cordond/Desktop/output_m_text.mp4"]
merge_videos_vertically(video_paths_merge, "/Users/cordond/Desktop/output_final.mp4")
