from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
#print(webpage)

soup = BeautifulSoup(webpage, "html.parser")
movies = []
#print(soup)
titles = soup.find_all(name="h3", class_="title")
#print(titles.getText())
for t in titles:
    title = t.getText()
    movies.append(title)

moviess = movies[::-1]
# for movie in movies:
#     print(movie)

with open(file="movies.txt", mode="w", encoding="utf8") as file:
    for title in moviess:
        file.write(f"{title}\n")
