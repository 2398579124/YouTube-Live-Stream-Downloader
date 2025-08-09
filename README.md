# YouTube-Live-Stream-Downloader
Automatic downloading, searching, and uploading (to a separate YouTube channel) of livestreams, designed to run indefinitely.
## Dependencies
[requires python 3.10+](https://wiki.python.org/moin/BeginnersGuide/Download)  
[pip installation guide](https://pip.pypa.io/en/stable/installation/)  
[ffmpeg installation guide](https://ffmpeg.org/download.html)  
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
Two files are needed to run this script (both of which are gotten through Google's API):  
`client_secret.json` (OAuth credentials)  
`token.pickle` (generated after the first run of the script using OAuth) (you will do this later)  
### Creating YouTube API token
1. Choose/create the account you want to use to upload the channel and get the API keys (it is easiest to keep these combined)
2. Create a project in the [Google Developers Console](https://console.cloud.google.com/apis/dashboard) and [obtain authorization credentials](https://developers.google.com/youtube/registering_an_application) for both an API key and OAuth (client_secret.json) (with the Google Acount you want to use)
3. After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:  
    - Go to the [API Console](https://console.cloud.google.com/) and select the project that you just registered.  
    - Visit the [Enabled APIs page](https://console.cloud.google.com/apis/enabled). In the list of APIs, make sure the status is ON for the YouTube Data API v3.
## Setting up the script
1. Downlaod all files and save them to a shared folder (eg. YouTubeDownlaoder)
2. Using your terminal cd into the folder where you saved the files
#### Run Create.py (`python Create.py`)
3. Follow the promts given (the API key is VERY important)
4. The script can try to find a YouTube channel by name but it may not be 100% accurate. To check it go to www.youtube.com/channel/[INPUT_YOUR_CHANNEL_ID]/
5. 28 minutes is recommended becase of the 10,000 API daily token limit. Each time the script checks it costs 100 tokens, and each video uploaded costs 1600 tokens.
#### Run Main.py (`python Main.py`)
6. This is the main script
7. When you run this script you should see a log like this: [CURRENT_DATE] no streams (if there are no current streams)
8. To get the `token.pickle` file you need to have a video be uploaded. To do this pick a youtuber who has a current livestream (go back to #3)
9. A Google sign in promt should open. Sign-in with the Google account you have your YouTube channel on.
10. You should see two new files now in your curent directory (run `ls` in your terminal to view this)  
    -- `token.picke`  
    -- `upload.txt` (This is where the ID of previously streamed livestreams goes to prevent duplicate downloads)  
11. If you are running this just in terminal you are done! Keep the `Main.py` script running at all times.
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
