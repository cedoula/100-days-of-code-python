from bs4 import BeautifulSoup
import requests
import spotipy
from keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from spotipy.oauth2 import SpotifyOAuth


BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_SEARCH_ENDPOINT = "https://api.spotify.com/v1/search"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = BILLBOARD_URL + date
response = requests.get(url)
billboard_page_html = response.text

soup = BeautifulSoup(billboard_page_html, "html.parser")

list_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

songs = [song.getText() for song in list_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=SPOTIFY_CLIENT_ID, 
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
song_uris = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{date[:4]}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
#print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)