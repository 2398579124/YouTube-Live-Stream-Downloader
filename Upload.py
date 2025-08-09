import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def upload_youtube_video(
    video_file_path: str,
    title: str,
    tags: list[str] = ["archival"],
    category_id: str = "25",
    description: str = """automatic archival""",
    privacy_status: str = "public",
    client_secrets_file: str = "client_secret.json",
    token_file: str = "token.pickle"
) -> str | None:

    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

    creds = None

    if os.path.exists(token_file):
        with open(token_file, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES
            )
            creds = flow.run_local_server(port=8080)

        with open(token_file, "wb") as token:
            pickle.dump(creds, token)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False,
        },
        "notifySubscribers": True
    }

    media_body = MediaFileUpload(video_file_path, chunksize=1024*1024, resumable=True)

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media_body,
    )

    from googleapiclient.errors import HttpError

    try:
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")
    except HttpError as e:
        if e.resp.status == 403 and b"quota" in e.content.lower():
            print("❌ Quota exceeded during upload. Stopping upload.")
            return None
        else:
            raise

    video_id = response.get("id")
    print(f"Upload complete: https://www.youtube.com/watch?v={video_id}")
    return video_id