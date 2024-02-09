from pytube import YouTube
from moviepy.editor import *


def download_video_and_convert_to_mp3(youtube_url, output_path):
    # Download the video from YouTube
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    download_path = video.download(
        output_path=output_path, filename='temp_video.mp4')

    # Load the downloaded video
    video_clip = VideoFileClip(download_path)

    # Extract audio from the video and save it as MP3
    mp3_filename = download_path.replace('.mp4', '.mp3')
    video_clip.audio.write_audiofile(mp3_filename)

    # Close the video file to free resources
    video_clip.close()

    # Remove the downloaded video file if only the audio is needed
    os.remove(download_path)

    return mp3_filename


youtube_url = 'YOUR_YOUTUBE_VIDEO_URL_HERE'
output_path = 'YOUR_DESIRED_OUTPUT_PATH'

mp3_file = download_video_and_convert_to_mp3(youtube_url, output_path)
print(f"Downloaded and converted to MP3: {mp3_file}")
