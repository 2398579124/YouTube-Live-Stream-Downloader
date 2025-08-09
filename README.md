# YouTube-Live-Stream-Downloader
Automatic downloading, searching, and uploading (to a separate YouTube channel) of livestreams, designed to run indefinitely.
## Dependencies
[requires python 3.10+](https://wiki.python.org/moin/BeginnersGuide/Download)  
[pip instalation guide](https://pip.pypa.io/en/stable/installation/)  
[ffmpeg instalation guide](https://ffmpeg.org/download.html)  
___
Run these commands to install the required Python dependencies
### Mac/Linux:
```bash
pip install --no-cache-dir \
    google-api-python-client \
    google-auth-oauthlib \
    google-auth-httplib2 \
    yt-dlp \
    requests
```
### Windows (PowerShell):
```bash
pip install --no-cache-dir google-api-python-client google-auth-oauthlib google-auth-httplib2 yt-dlp requests
```
___
## YouTube API token & setting up OAuth
Two files are needed to run this script: client_secret.json & token.pickle, both of which are gotten through google's API
### Creating YouTube API token
1. Choose/create the acount you want to use to upload the channel (it is easiest to keep these combined)
2. Create a project in the [Google Developers Console](https://console.cloud.google.com/apis/dashboard) and [obtain authorization credentials](https://developers.google.com/youtube/registering_an_application) for both an API key and OAuth (client_secret.json) (with the google acount you want to use)
3. After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:  
    - Go to the [API Console](https://console.cloud.google.com/) and select the project that you just registered.  
    - Visit the [Enabled APIs page](https://console.cloud.google.com/apis/enabled). In the list of APIs, make sure the status is ON for the YouTube Data API v3.
