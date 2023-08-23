import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"


def get_songs_info(date):
    resp = requests.get(f"{URL}{date}")
    resp.raise_for_status()
    html_content = resp.text

    soup = BeautifulSoup(html_content, "html.parser")

    chart = soup.find("div", {"class": "chart-results-list"})

    song_entry = chart.find_all("div", {"class": "o-chart-results-list-row-container"})

    songs = []
    for entry in song_entry:
        song_name = entry.find("h3", {"class": "c-title"}).getText().strip()
        artist = entry.find("li", {"class": "lrv-u-width-100p"}).find("span").getText().strip()
        songs.append({"track": song_name, "artist": artist})

    return songs
