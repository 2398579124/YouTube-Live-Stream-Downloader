import requests

class YouTubeQuotaExceeded(Exception):
    pass

class YouTubeAPIError(Exception):
    pass

def GetLiveStreams(API_KEY, CHANNELID):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "id,snippet",
        "channelId": CHANNELID,
        "eventType": "live",
        "type": "video",
        "maxResults": 10,
        "key": API_KEY,
    }

    data = requests.get(url, params=params).json()

    # Handle API errors explicitly
    if "error" in data:
        reason = data["error"]["errors"][0].get("reason", "")
        message = data["error"].get("message", "Unknown API error")
        if reason == "quotaExceeded":
            raise YouTubeQuotaExceeded(message)
        else:
            raise YouTubeAPIError(message)

    livestreams = []

    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        livestreams.append({
            "title": item["snippet"]["title"],
            "video_id": video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })

    return livestreams
