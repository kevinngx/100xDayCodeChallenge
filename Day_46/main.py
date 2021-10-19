import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


SPOTIFY_BASE_ADDRESS = "https://api.spotify.com"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/2008-01-05"
OAUTH_TOKEN = "BQDjNihy0ODOOyD6EFjgJC52pnWhR8Cvb7ldqeKj8bjCg2O9RSwQlPnEKyFsCegkUKhH55_wb1O8yHC1_UlK1eCmAcS6g3YE0y2A4UUVbA2zErLYmSpNBIxlcw6FrBnUmJHy2upll20nsUw"

USER_ID = "1245266985"
REDIRECT_URI = "http://127.0.0.1:9090"
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

def main():
    scope = "playlist-modify-private" # Check privilege herehttps://developer.spotify.com/documentation/general/guides/scopes/
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    print(sp.user_playlists(USER_ID))
    

def getChart():
    response = requests.get(BILLBOARD_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    chart_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    chart_artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")

    songs = []
    artists = []

    for artist in chart_artists:
        artists.append(artist.getText())

    for song in chart_songs:
        songs.append(song.getText())
    
    count = 0
    for song in songs:
        print(str(count + 1) + ". " + songs[count] + " - " + artists[count])
        count += 1

def insertTrack():
    print("Track Inserted")

def createPlaylist():

    print("Playlist Created")

if __name__ == "__main__":
    main()