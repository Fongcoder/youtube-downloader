# YouTube Video Downloader GUI

A simple Python GUI application to download multiple YouTube videos in the highest quality using yt-dlp.

## Features
- Add multiple YouTube video links to a list
- Remove links from the list
- Download all videos at once in the best quality
- Progress and status shown in the app

## Requirements
- Python 3.x
- yt-dlp
- FFmpeg

## Installation
```bash
pip install yt-dlp
```

Download and install FFmpeg from [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/) and add it to your PATH.

## Usage
1. Run the GUI script:
   ```bash
   python youtube_downloader_gui.py
   ```
2. Paste YouTube video URLs one by one and click "Add URL".
3. Click "Download All" to download all videos to your Downloads folder.

All videos will be saved to `C:/Users/Albit/Downloads` by default.
