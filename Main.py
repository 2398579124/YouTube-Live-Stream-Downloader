import ctypes
import time
import Download # type: ignore
import IsLive # type: ignore
import json
from datetime import datetime

# Prevent sleep
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

try:
    with open("config.json", "r") as f:
        config = json.load(f)
    API_KEY = config["API_KEY"]
    CHANNELID = config["CHANNELID"]
    WAIT = config["WAIT"]

    while True:
        Streams = IsLive.GetLiveStreams(API_KEY, CHANNELID)
        if Streams:
            print(f"Found {len(Streams)} live stream(s):")
            for Stream in Streams:
                print(f" Stream {len(Stream) + 1} - {Stream['title']}: {Stream['url']} - id:{Stream['video_id']}")
                Download.DownloadVideo(Stream["video_id"])
        else:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] no stream")
            time.sleep(int(WAIT) * 60)
finally:
    # Re-enable sleep (important!)
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)