import yt_dlp

def DownloadVideo(VideoId):
    url = f"https://www.youtube.com/watch?v={VideoId}"

    options = {
        "live_from_start": True,
        "hls_use_mpegts": True,
        "outtmpl": "%(title)s.%(ext)s",        # clean filename
        "merge_output_format": "mp4",          # merge into a single mp4 file
        "outtmpl": "%(title).200s.%(ext)s",    # Limit the max length to 200 characters  
        "max_filesize": 10_000_000_000,                 # Limit file size to 10 gigabytes
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
