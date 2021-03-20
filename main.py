from bs4 import BeautifulSoup
import requests

bb_search = input("Find out what the top 100 songs were the year you were born! \nWrite your birthdate in this format YYYY-MM-DD\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{bb_search}")
bb_search = response.text

soup = BeautifulSoup(bb_search, "html.parser")
song_data = soup.findAll(name="span", class_="chart-element__information__song")

songs = []

for song in song_data:
    song = song.getText()
    songs.append(song)

artists = [artist.getText() for artist in soup.findAll(name="span", class_="chart-element__information__artist")]

print(songs)
print(artists)