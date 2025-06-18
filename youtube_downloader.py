import yt_dlp

def download_video(url, path='C:\\Users\\Albit\\Downloads'):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # highest quality video+audio
        'outtmpl': f'{path}\\%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    download_video(video_url)
