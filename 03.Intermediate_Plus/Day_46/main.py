import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

USER_ID = "1245266985"

def main():
    target_date = input("Enter year in format YYYY-MM-DD : ")

    playlist_uris = []
    for song in getChart(target_date):
        playlist_uris.append(getTrackURI(song))
    print("Log | URIs Retrieved")

    playlist_id  = createPlaylist(target_date)
    insertTracks(playlist_uris, playlist_id)

    print("Log | Program Completed")


def getChart(target_date):
    
    chart_url = "https://www.billboard.com/charts/hot-100/" + target_date

    response = requests.get(chart_url)
    soup = BeautifulSoup(response.text, "html.parser")
    chart_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    
    songs = []
    for song in chart_songs:
        songs.append(song.getText())
    
    print("Log | Top Charts Retrieved")
    return songs

def insertTracks(songs, playlist_id):
    scope = "playlist-modify-private" # Check privilege here https://developer.spotify.com/documentation/general/guides/scopes/
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_add_items(playlist_id, songs)

    print("Log | Tracks Inserted")

def getTrackURI(song):
    scope = "playlist-modify-private" # Check privilege herehttps://developer.spotify.com/documentation/general/guides/scopes/
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    response = sp.search(song, limit=1, type='track')
    try:
        URI = response["tracks"]["items"][0]["uri"]
        print(f'URI Retrieved: {URI}')
    except:
        print(f'Song not found: {song}')
        URI = "spotify:track:4cOdK2wGLETKBW3PvgPWqT"
    return URI

def createPlaylist(target_date):
    scope = "playlist-modify-private" # Check privilege here https://developer.spotify.com/documentation/general/guides/scopes/
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    response = sp.user_playlist_create(USER_ID, "Throwback Charts - " + target_date, public=False)
    playlist_id = response["id"]

    print("Log | Playlist Created")
    return playlist_id

if __name__ == "__main__":
    main()