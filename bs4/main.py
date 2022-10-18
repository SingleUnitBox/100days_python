from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
#print(articles)
for article_tag in articles:
    article_tag = article_tag.find(name="a")
    #print(article_tag)
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(article_texts[index], article_links[index])








# with open(file="website.html", encoding="utf8") as file:
#     contents = file.read()
#     #print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
# print(section_heading.getText())
# print(section_heading.name)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#ID
# name = soup.select_one(selector="#name")
# print(name)
#CLASS
# headings = soup.select(selector=".heading")
# print(headings)