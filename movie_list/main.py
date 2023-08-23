import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


resp = requests.get(URL)
resp.raise_for_status()
html_content = resp.text

soup = BeautifulSoup(html_content, "html.parser")

gallery = soup.find("div", {"class": "gallery"})

films = gallery.find_all("h3", {"class": "title"})

list_of_films = [f.getText() for f in films]

with open("films.txt", "w", encoding="UTF8") as file:
    for film in list_of_films[::-1]:
        file.write(f"{film}\n")


