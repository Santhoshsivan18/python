# import os
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from flask import Flask, request, redirect, session, url_for
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow

# app = Flask(__name__)
# app.secret_key = os.urandom(24)
# app.config["SESSION_COOKIE_NAME"] = "spotify_cookie"

# SPOTIPY_CLIENT_ID = "ab93990d09744f2d8c6882c5335a1dbf"
# SPOTIPY_CLIENT_SECRET = "657cb5736f454711afea307fce053a74"
# SPOTIPY_REDIRECT_URI = "http://localhost:8080"
# SCOPE = "playlist-read-private playlist-read-collaborative"

# sp_oauth = SpotifyOAuth(
#     client_id=SPOTIPY_CLIENT_ID,
#     client_secret=SPOTIPY_CLIENT_SECRET,
#     redirect_uri=SPOTIPY_REDIRECT_URI,
#     scope=SCOPE,
# )

# @app.route("/")
# def index():
#     auth_url = sp_oauth.get_authorize_url()
#     return redirect(auth_url)

# @app.route("/callback")
# def callback():
#     code = request.args.get("code")
#     token_info = sp_oauth.get_access_token(code)
#     session["token_info"] = token_info
#     return redirect(url_for("create_playlist"))

# @app.route("/create_playlist")
# def create_playlist():
#     token_info = session.get("token_info")
#     if not token_info:
#         return redirect(url_for("index"))

#     sp = spotipy.Spotify(auth=token_info["access_token"])
#     playlist_id = "78q8eeZl672T0uxWjI3pGQ"  # Example public playlist ID
#     results = sp.playlist_tracks(playlist_id)
#     songs = [track["track"]["name"] for track in results["items"]]

#     # Authenticate with YouTube
#     flow = InstalledAppFlow.from_client_secrets_file(
#         "client_secret.json", scopes=["https://www.googleapis.com/auth/youtube"]
#     )
#     credentials = flow.run_local_server(port=0)
#     youtube = build("youtube", "v3", credentials=credentials)

#     # Create YouTube Playlist
#     request = youtube.playlists().insert(
#         part="snippet",
#         body={
#             "snippet": {
#                 "title": "New Playlist",
#                 "description": "Created with Python",
#                 "tags": ["sample playlist"],
#                 "defaultLanguage": "en",
#             }
#         },
#     )
#     response = request.execute()
#     youtube_playlist_id = response["id"]

#     # Add Songs to YouTube Playlist
#     for song in songs:
#         search_response = (
#             youtube.search()
#             .list(q=f"{song} lyrics", part="snippet", maxResults=1)
#             .execute()
#         )
#         video_id = search_response["items"][0]["id"]["videoId"]
#         youtube.playlistItems().insert(
#             part="snippet",
#             body={
#                 "snippet": {
#                     "playlistId": youtube_playlist_id,
#                     "resourceId": {"kind": "youtube#video", "videoId": video_id},
#                 }
#             },
#         ).execute()

#     return "Playlist created successfully on YouTube!"

# if __name__ == "__main__":
#     app.run(port=8888)


import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your credentials and redirect URI
SPOTIPY_CLIENT_ID = "ab93990d09744f2d8c6882c5335a1dbf"
SPOTIPY_CLIENT_SECRET = "657cb5736f454711afea307fce053a74"
SPOTIPY_REDIRECT_URI = "http://localhost:8080"  # Or your chosen redirect URI

# Authenticate using SpotifyOAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-read-private playlist-read-collaborative",
    )
)


def fetch_playlist_tracks(playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = results["items"]

        # Print track names
        for idx, item in enumerate(tracks):
            track = item["track"]
            print(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")
    except spotipy.exceptions.SpotifyException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example playlist IDs
public_playlist_id = "78q8eeZl672T0uxWjI3pGQ"  # Public playlist
# private_playlist_id = "37i9dQZF1DX7vl8XKmpwdM"  # Private playlist (must have access)

# Fetch tracks from public playlist
fetch_playlist_tracks(public_playlist_id)
# Fetch tracks from private playlist (requires access)
# fetch_playlist_tracks(private_playlist_id)



# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow

# # YouTube Authentication
# flow = InstalledAppFlow.from_client_secrets_file(
#     "client_secret.json", scopes=["https://www.googleapis.com/auth/youtube"]
# )
# credentials = flow.run_console()
# youtube = build("youtube", "v3", credentials=credentials)

# # Fetch Spotify Playlist
# playlist_id = "your_spotify_playlist_id"
# results = sp.playlist_tracks(playlist_id)
# songs = [track["track"]["name"] for track in results["items"]]

# # Create YouTube Playlist
# request = youtube.playlists().insert(
#     part="snippet",
#     body={
#         "snippet": {
#             "title": "New Playlist",
#             "description": "Created with Python",
#             "tags": ["sample playlist"],
#             "defaultLanguage": "en",
#         }
#     },
# )
# response = request.execute()
# playlist_id = response["id"]

# # Add Songs to YouTube Playlist
# for song in songs:
#     search_response = (
#         youtube.search()
#         .list(q=song + " lyrics", part="snippet", maxResults=1)
#         .execute()
#     )
#     video_id = search_response["items"][0]["id"]["videoId"]
#     youtube.playlistItems().insert(
#         part="snippet",
#         body={
#             "snippet": {
#                 "playlistId": playlist_id,
#                 "resourceId": {"kind": "youtube#video", "videoId": video_id},
#             }
#         },
#     ).execute()
