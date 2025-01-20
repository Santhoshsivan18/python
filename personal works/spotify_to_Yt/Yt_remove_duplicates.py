from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd

CLIENT_SECRET_FILE = "client_secret.json"
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]

# Authenticate and construct the service
credentials = service_account.Credentials.from_service_account_file(
    CLIENT_SECRET_FILE, scopes=SCOPES)
service = build(API_NAME, API_VERSION, credentials=credentials)

playlist_id = "PL_jlEiP3TGApyZCeslcivyADinOdhP-AA"

response = service.playlistItems().list(
    part="contentDetails",
    playlistId=playlist_id,
    maxResults=50
).execute()

playlistItems = response["items"]
nextPageToken = response.get("nextPageToken")

while nextPageToken:
    response = service.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=nextPageToken
    ).execute()
    
    playlistItems.extend(response["items"])
    nextPageToken = response.get("nextPageToken")
