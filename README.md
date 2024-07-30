# YouTube Video Downloader with Subtitles

## Overview

This project provides a Python script that allows you to download YouTube videos in 1080p quality along with their subtitles using the `yt-dlp` library. The script can be run in either interactive mode, where users can input YouTube URLs one by one, or script mode, which uses a predefined list of URLs.

## Features

- Downloads YouTube videos in 1080p quality.
- Merges video and audio files.
- Downloads and embeds VTT subtitles.
- Checks for existing videos to avoid duplicate downloads.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/TeomanEgeSelcuk/Install-YouTube-Vids.git
    cd yt-video-downloader
    ```

2. **Set up the Conda environment:**

    Create a Conda environment using the provided environment file.

    ```sh
    conda env create -f install_yt_vids_env.yaml
    conda activate install_yt_vids_env
    ```

3. **Install dependencies:**

    Install additional dependencies using Poetry.

    ```sh
    poetry install
    ```

## Usage

1. **Interactive Mode:**

    In interactive mode, users can input YouTube URLs one by one. The script will prompt users to enter URLs and will download the videos and subtitles accordingly.

    ```sh
    python main.py
    ```

    When prompted, enter `1` to select interactive mode:

    ```
    Enter mode (1 for interactive, 2 for script): 1
    ```

    Then input YouTube URLs one by one, typing `done` when finished:

    ```
    YouTube URL: https://www.youtube.com/watch?v=example1
    YouTube URL: https://www.youtube.com/watch?v=example2
    YouTube URL: done
    ```

2. **Script Mode:**

    In script mode, the script uses a predefined list of YouTube URLs to download videos and subtitles.

    ```sh
    python main.py
    ```

    When prompted, enter `2` to select script mode:

    ```
    Enter mode (1 for interactive, 2 for script): 2
    ```

    Edit the `script_mode` function in `main.py` to include your list of YouTube URLs:

    ```python
    def script_mode(output_dir: str) -> None:
        youtube_urls = [
            'https://www.youtube.com/watch?v=example1',
            'https://www.youtube.com/watch?v=example2',
            # Add more URLs here
        ]
        for url in youtube_urls:
            if video_exists(url, output_dir):
                print(f"Video already exists: {url}")
                continue
            download_video(url, output_dir)
            download_vtt_subtitle(url, output_dir)
    ```

## Project Structure

- `main.py`: Contains the main script with functions to download videos, subtitles, and run in interactive or script mode.
- `install_yt_vids_env.yaml`: Conda environment file to set up dependencies.
- `pyproject.toml`: Poetry configuration file for managing dependencies and project settings.

## Functions

### `download_video(youtube_url: str, output_dir: str) -> None`

Download a YouTube video and save it as an mp4 file in the specified output directory.

**Example usage:**

```python
download_video("https://www.youtube.com/watch?v=-pSf9_MgsZ4", "/videos")
```

### `download_vtt_subtitle(youtube_url: str, output_dir: str) -> None`

Download VTT subtitles for a YouTube video and save them in the specified output directory.

**Example usage:**

```python
download_vtt_subtitle("https://www.youtube.com/watch?v=-pSf9_MgsZ4", "/videos")
```

### `video_exists(youtube_url: str, output_dir: str) -> bool`

Check if the video corresponding to the given YouTube URL already exists in the output directory.

**Example usage:**

```python
video_exists("https://www.youtube.com/watch?v=-pSf9_MgsZ4", "/videos")
```

### `interactive_mode(output_dir: str) -> None`

Run the interactive mode where users can input YouTube URLs to download videos and subtitles.

**Example usage:**

```python
interactive_mode("/videos")
```

### `script_mode(output_dir: str) -> None`

Run the script mode where a predefined list of YouTube URLs are used to download videos and subtitles.

**Example usage:**

```python
script_mode("/videos")
```

## Authors

- Teoman Selcuk - [teomanege.selcuk@gmail.com](mailto:teomanege.selcuk@gmail.com)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---
