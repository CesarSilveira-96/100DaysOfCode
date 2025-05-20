import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(f"{URL}")
soup = BeautifulSoup(response.text, "html.parser")

# Seleciona os 100 primeiros filmes
movie_list = soup.select("div.article-title-description__text > h3.title")[:100]
titles_list = []

for i in range(0,100):
    movie_title = movie_list[i].get_text()
    titles_list.append(movie_title)

final_list = titles_list[::-1]
print(final_list)

with open("movies.txt", mode="a", encoding="utf-8") as movies_file:
    for i in range(0,100):
        movies_file.write(f"{final_list[i]}\n")