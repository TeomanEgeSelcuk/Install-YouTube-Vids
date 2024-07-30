import os
import sys
from yt_dlp import YoutubeDL

def download_video(youtube_url: str, output_dir: str) -> None:
    """
    Download a YouTube video and save it as an mp4 file in the specified output directory.

    Args:
        youtube_url (str): URL of the YouTube video to download.
        output_dir (str): Directory to save the downloaded video.

    Example usage:
        download_video("https://www.youtube.com/watch?v=-pSf9_MgsZ4", "/videos")
        This will download the video from the provided URL and save it as an mp4 file in the /videos directory.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Set options for YoutubeDL
    ydl_opts = {
        'format': '(bestvideo[height<=1080][ext=mp4]/bestvideo)+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    # Download the video
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def download_vtt_subtitle(youtube_url: str, output_dir: str) -> None:
    """
    Download VTT subtitles for a YouTube video and save them in the specified output directory.

    Args:
        youtube_url (str): URL of the YouTube video to download subtitles for.
        output_dir (str): Directory to save the downloaded subtitles.

    Example usage:
        download_vtt_subtitle("https://www.youtube.com/watch?v=-pSf9_MgsZ4", "/videos")
        This will download the subtitles for the video from the provided URL and save them in the /videos directory.
    """
    # Set options for YoutubeDL
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'vtt',
        'subtitleslangs': ['en'],
        'skip_download': True,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    # Download the subtitles
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def video_exists(youtube_url: str, output_dir: str) -> bool:
    """
    Check if the video corresponding to the given YouTube URL already exists in the output directory.

    Args:
        youtube_url (str): URL of the YouTube video to check.
        output_dir (str): Directory to check for the existing video.

    Returns:
        bool: True if the video exists, False otherwise.
    """
    # Extract the video title
    ydl_opts = {'skip_download': True, 'quiet': True, 'outtmpl': '%(title)s.%(ext)s'}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        video_title = info_dict.get('title', None)

    if video_title:
        # Check if the file exists in the output directory
        return any(file.startswith(video_title) for file in os.listdir(output_dir))
    return False

def interactive_mode(output_dir: str) -> None:
    """
    Run the interactive mode where users can input YouTube URLs to download videos and subtitles.

    Args:
        output_dir (str): Directory to save the downloaded videos and subtitles.

    Example usage:
        interactive_mode("/videos")
        This will prompt the user to enter YouTube URLs and save the videos and subtitles in the /videos directory.
    """
    print("Interactive Mode: Enter YouTube URLs (one per line). Type 'done' when finished.")
    urls = []
    while True:
        url = input("YouTube URL: ")
        if url.lower() == 'done':
            break
        urls.append(url)

    for url in urls:
        if video_exists(url, output_dir):
            print(f"Video already exists: {url}")
            continue
        download_video(url, output_dir)
        download_vtt_subtitle(url, output_dir)

def script_mode(output_dir: str) -> None:
    """
    Run the script mode where a predefined list of YouTube URLs are used to download videos and subtitles.

    Args:
        output_dir (str): Directory to save the downloaded videos and subtitles.

    Example usage:
        script_mode("/videos")
        This will download videos and subtitles from the predefined list of URLs and save them in the /videos directory.
    """
    youtube_urls = [
        # Add your list of YouTube URLs here
        'https://www.youtube.com/watch?v=-pSf9_MgsZ4&ab_channel=Fireship',
        'https://www.youtube.com/watch?v=b1aBzAE-IFY',
        # ...
    ]
    for url in youtube_urls:
        if video_exists(url, output_dir):
            print(f"Video already exists: {url}")
            continue
        download_video(url, output_dir)
        download_vtt_subtitle(url, output_dir)

if __name__ == "__main__":
    mode = input("Enter mode (1 for interactive, 2 for script): ").strip()
    output_dir = "/videos"  # Specify your output directory here

    if mode == '1':
        interactive_mode(output_dir)
    elif mode == '2':
        script_mode(output_dir)
    else:
        print("Invalid mode. Please enter '1' for interactive or '2' for script.")
        sys.exit(1)
