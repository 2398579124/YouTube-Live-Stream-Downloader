import yt_dlp

def DownloadVideo(VideoId):
    url = f"https://www.youtube.com/watch?v={VideoId}"

    options = {
        "live_from_start": True,
        "hls_use_mpegts": True,
        "merge_output_format": "mp4",          # merge into a single mp4 file
        "outtmpl": "%(title).85s.%(ext)s",    # Limit the max length to 85 characters  
        "max_filesize": 10_000_000_000,                 # Limit file size to 10 gigabytes
        "format": "bestvideo[height<=1080]+bestaudio/best",  # pick best ≤1080p, else fallback
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        return ydl.prepare_filename(ydl.extract_info(url, download=True))