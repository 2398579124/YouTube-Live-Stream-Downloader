import time
import Download  # type: ignore
import IsLive    # type: ignore
import Upload    # type: ignore
import json
import os
from datetime import datetime

if os.path.exists("upload.txt"):
    with open("upload.txt", "r") as f:
        uploadtxt = set(line.strip() for line in f if line.strip())
else:
    uploadtxt = set()

with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config["API_KEY"]
CHANNELID = config["CHANNELID"]
WAIT = config["WAIT"]

while True:
    try:
        Streams = IsLive.GetLiveStreams(API_KEY, CHANNELID)
        if Streams:
            print(f"Found {len(Streams)} live stream(s):")
            for i, Stream in enumerate(Streams, start=1):
                uploadid = Stream["video_id"]
                if uploadid in uploadtxt:
                    print(f" Stream {i} already uploaded. Skipping.")
                    continue
                print(f" Stream {i} - {Stream['title']}: {Stream['url']} - id:{Stream['video_id']}")
                videopath = Download.DownloadVideo(Stream["video_id"])
                if not os.path.exists(videopath) or os.path.getsize(videopath) == 0:
                    print(f"Missing downlaod {videopath}")
                    continue
                print(f"{Stream['title'][:85]}.mp4")
                with open("upload.txt", "a") as f:
                    f.write(f"{uploadid}\n")
                uploadtxt.add(uploadid)
                Upload.upload_youtube_video(video_file_path=videopath, title=f"ARCHIVAL: {Stream['title']}")
                print(f"deleting {videopath}")
                os.remove(videopath)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] stream(s) already uploaded")
            time.sleep(int(WAIT) * 60)

        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] no streams")
            time.sleep(int(WAIT) * 60)

    except IsLive.YouTubeQuotaExceeded as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Quota exceeded: {e}")
        time.sleep(3600)
        continue
        
    except IsLive.YouTubeAPIError as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] API error: {e}")
        time.sleep(3600)
        continue

    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Unexpected error: {e}")
        break
