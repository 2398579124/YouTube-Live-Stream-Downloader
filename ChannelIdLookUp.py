import requests

def ChannelIdLookUp(API_KEY, username):
    url = (
        f'https://www.googleapis.com/youtube/v3/search?part=snippet'
        f'&q={username}&type=channel&key={API_KEY}'
    )
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        # Try to find exact match on channel title (case-insensitive)
        for item in data['items']:
            title = item['snippet']['channelTitle']
            if title.lower() == username.lower():
                return item['snippet']['channelId']
        # If no exact match, return the first channel's ID as fallback
        if data['items']:
            return data['items'][0]['snippet']['channelId']
    return None