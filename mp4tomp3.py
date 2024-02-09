from moviepy.editor import *


def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    # Load the video file
    video = VideoFileClip(mp4_file_path)

    # Extract the audio from the video
    audio = video.audio

    # Write the audio to a new MP3 file
    audio.write_audiofile(mp3_file_path)

    # Close the video file
    video.close()


mp4_file_path = 'path/to/your/video.mp4'
mp3_file_path = 'path/to/your/audio.mp3'

convert_mp4_to_mp3(mp4_file_path, mp3_file_path)
