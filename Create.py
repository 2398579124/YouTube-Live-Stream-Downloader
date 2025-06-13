import ChannelIdLookUp # type: ignore
import IsLive # type: ignore
import json

API_KEY = ''
CHANNEL = ''
CHANNELID = ''
WAIT = 20

if (API_KEY := input("What is your YouTube API key?\n")) == "":
    API_KEY = 'AIzaSyAcz39G2DYE3rHaOVkIKs_Hl27rJsK8cwU'  # fallback default

if input('Do you want to try to find a channel using a handle? (y/n)\n') == 'y':
    CHANNELID = ChannelIdLookUp.ChannelIdLookUp(API_KEY, input('Please input the handle name: \n'))
    if input(f'is this the correct channel ID?: {CHANNELID} (y/n)\n') == "n":
        CHANNELID = input("Please input channel ID manually: \n")
    else:
        pass
else:
    CHANNELID = input("Please input your channel ID (ex: UCX6OQ3DkcsbYNE6H8uQQuVA):\n")

WAIT = input("How often would you like this script to check for a live stream? (20 minute recommended)\n")

config = {
    "API_KEY": API_KEY,
    "CHANNELID": CHANNELID,
    "WAIT": WAIT
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

print('\n')
