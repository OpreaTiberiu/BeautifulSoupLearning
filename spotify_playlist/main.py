import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from spotify_playlist.billboard_soup import get_songs_info

load_dotenv()

date = "1996-01-09"#input("What date do you want for this playlist? ('YYYY-MM-DD' format): ")

songs = get_songs_info(date)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["spotify_client_id"],
                                               client_secret=os.environ["spotify_client_secret"],
                                               redirect_uri=os.environ["redirect_link"],
                                               scope="playlist-modify-private"))

u = sp.current_user()

links = []
for song in songs:
    spotify_search_result = sp.search(q=f"artist:{song['artist']} track:{song['track']}")
    if len(spotify_search_result["tracks"]["items"]) > 0:
        links.append(spotify_search_result["tracks"]["items"][0]["uri"])

playlist = sp.user_playlist_create(name=f"{date} Billboard 100", public=False, user=u["id"])

sp.playlist_add_items(playlist["id"], links)
