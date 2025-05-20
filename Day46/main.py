import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

USER_ID = "cesarsilveira18"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id="1bf0721134fb42f9a1563946242255a9",
        client_secret="05debd6b755144f9a60c5352ae7664ec",
        show_dialog=True,
        cache_path="token.txt",
    username="César Silveira",
    )
)
user_id = sp.current_user()["id"]


BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

# date_choice = input("Write the date you would like to travel to. The only format accepted will be YYYY-MM-DD:\n")
date_choice = "1999-06-06"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/136.0.0.0 Safari/537.36"
}

bb_response = requests.get(f"{BILLBOARD_URL}{date_choice}", headers=header)
soup = BeautifulSoup(bb_response.text,"html.parser")
songs_data = soup.select(selector="li h3#title-of-a-story")
songs_list = [songs_data[i].get_text() for i in range(0, 100)]
final_songs_list = []
artists_list = []

for artist_tag in soup.select('li.o-chart-results-list__item span.c-label'):
    artist = artist_tag.get_text(strip=True)
    # Evita capturar entradas em branco ou duplicadas como "NEW" ou "RE-ENTRY"
    if artist not in map(str, range(1, 101)) and artist not in ["NEW", "RE-ENTRY", "-", "RE-\nENTRY"]:
        artists_list.append(artist)

for i in range(0,100):
    # Song Titles
    split_title_list = songs_list[i].split()
    song_tittle = ""
    for word in split_title_list:
        song_tittle += word
        if len(split_title_list) > 1 and split_title_list.index(word) < (len(split_title_list)-1):
            song_tittle += " "
    final_songs_list.append(song_tittle)

# print(artists_list)
# print(len(artists_list))
# print(final_songs_list)
# print(len(final_songs_list))

# USING THE SPOTIFY API

with open("token.txt") as token_file:
    data = token_file.read()
    json_data = json.loads(data)
    token = json_data["access_token"]

sp = spotipy.Spotify(auth=token)

# PLAYLIST CREATION
# playlist_info = {
#     "name": f"Billboard Hot 100 from {date_choice}"
# }
#
# playlist_header = {
#     "Authorization": f"Bearer {token}"
# }

playlist = sp.user_playlist_create(user=USER_ID, name=f"Billboard Hot 100 from {date_choice}", public=False)
print("Playlist criada com sucesso:", playlist["external_urls"]["spotify"])

track_uris = []

for song, artist in zip(final_songs_list, artists_list):
    result = sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print(f"Música não encontrada no Spotify: {song} - {artist}")

sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)


