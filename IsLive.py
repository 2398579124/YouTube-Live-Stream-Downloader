import requests

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

    livestreams = []

    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            livestreams.append({
                "title": title,
                "video_id": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })

    return livestreams
