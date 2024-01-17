from video_utils import *

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
