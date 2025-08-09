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
