# YouTube-Live-Stream-Downloader
Automatically downloads, searches for, and uploads livestreams (to a separate YouTube channel). Designed to run indefinitely.
## Dependencies
[requires Python 3.10+](https://wiki.python.org/moin/BeginnersGuide/Download)  
[pip installation guide](https://pip.pypa.io/en/stable/installation/)  
[FFmpeg installation guide](https://ffmpeg.org/download.html)  
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
```powershell 
pip install --no-cache-dir google-api-python-client google-auth-oauthlib google-auth-httplib2 yt-dlp requests
```
___
## YouTube API token & setting up OAuth
Two files are needed to run this script:  
`client_secret.json` (OAuth credentials, downloaded from Google)  
`token.pickle` (Generated automatically after the first run of the script using OAuth)
### Creating YouTube API token
1. Choose/create the account you want to use to upload the channel and get the API keys (using the same account for both is easiest)
2. Create a project in the [Google Developers Console](https://console.cloud.google.com/apis/dashboard) and [obtain authorization credentials](https://developers.google.com/youtube/registering_an_application) for both an API key and OAuth (client_secret.json) (with the Google Account you want to use)
3. After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:  
    - Go to the [API Console](https://console.cloud.google.com/) and select the project that you just registered.  
    - Visit the [Enabled APIs page](https://console.cloud.google.com/apis/enabled). In the list of APIs, make sure the status is ON for the YouTube Data API v3.
## Setting up the script
1. Download all files and save them to a shared folder (eg. YouTubeDownloader)
2. Using your terminal cd into the folder where you saved the files
#### Run Create.py (`python Create.py`)
3. Follow the prompts given (the API key is VERY important)
4. The script can try to find a YouTube channel by name but it may not be 100% accurate. To verify, go to www.youtube.com/channel/[INPUT_YOUR_CHANNEL_ID]/
5. A check interval of 28 minutes is recommended because of the 10,000 API daily token limit. Each time the script checks it costs 100 tokens, and each video uploaded costs 1600 tokens.
#### Run Main.py (`python Main.py`)
6. This is the main script
7. When there are no streams, `[CURRENT_DATE] no streams` is displayed (this is what you will probably see first)
8. To get the `token.pickle` file you need to have a video be uploaded. To do this pick a Youtuber who has a current livestream (go back to #3)
9. A Google sign-in promt should open. Sign-in on the same google acount as your archival YouTube channel's.
10. You should see two new files now in your current directory (run `ls` in your terminal to view this)  
    -- `token.picke`  
    -- `upload.txt` (This is where the video ID of previously streamed livestreams goes to prevent duplicate downloads)  
11. If you are running this in terminal you are done! Keep the `Main.py` script running at all times.
## Creating a Docker image
first ensure all your script settings are correct, you will not be able to change them later.  
Make sure [Docker](https://docs.docker.com/desktop/) is installed 
1. Still in the terminal, in your folder run this command:
```bash
docker build -t youtube-archiver .
docker save youtube-archiver -o youtube-archiver.tar    
   ```
2. A file named `youtube-archiver.tar` should have been saved to your computer.
3. You can run this image on any NAS or server with Docker installed
4. For more tips see the [Docker Documentation](https://docs.docker.com/)
## Troubleshooting / Tips
### Editing YouTube uploads.
For video download settings (eg. resolution) see `Download.py`, lines 3-13, in the "options" variable ([see yt_dpl documentation](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#usage-and-options))
For video upload settings (eg. description) see `Upload.py`, lines 10-19, in the  function parameters for upload_youtube_video() ([see Google documentation](https://developers.google.com/youtube/v3/docs/videos/insert)
