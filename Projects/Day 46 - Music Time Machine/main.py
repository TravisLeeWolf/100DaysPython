import art
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID='ID'
SPOTIPY_CLIENT_SECRET='SECRET'
SPOTIPY_REDIRECT_URI='URI'

SCOPE = "SCOPE"

print(art.logo)
userDate = input("Which date do you want to travel back to?\nType the date in this format YYYY-MM-DD: ")
year = userDate.split("-")[0]
billboardWebAddress = "https://www.billboard.com/charts/hot-100/"
finalWebAddress = f"{billboardWebAddress}{userDate}"

response = requests.get(finalWebAddress)
response.raise_for_status()
webSoup = BeautifulSoup(response.text, "html.parser")

songTags = webSoup.find_all(class_="chart-element__information__song")
songTitles = [songs.get_text() for songs in songTags]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, scope=SCOPE, redirect_uri=SPOTIPY_REDIRECT_URI))

trackURIs = []
for songTitle in songTitles:
    query = f"track: {songTitle} year: {year}"
    song = sp.search(query, 1, type="track")
    uri = song["tracks"]["items"][0]["uri"]
    trackURIs.append(uri)

print(trackURIs)