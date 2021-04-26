from bs4 import BeautifulSoup
import requests

# with open("website.html", "r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# #print(soup.title)
# #print(soup.title.string)

# all_anchor_tags = soup.find_all(name="a")

# #for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))

# #heading = soup.find(name="h1", id="name")
# #print(heading)

# #section_heading = soup.find(name="h3", class_="heading")
# #print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# response = requests.get("https://news.ycombinator.com/news")

# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title)

# articles = soup.find_all(name="a", class_="storylink")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
    
#     link = article_tag.get("href")
#     article_links.append(link)


# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# #print(article_texts)
# #print(article_links)
# print(article_upvotes)

# #print(article_upvotes[0].split()[0])

# index_max = article_upvotes.index(max(article_upvotes))
# print(article_texts[index_max])
# print(article_links[index_max])

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_web_page_html = response.text

soup = BeautifulSoup(empire_web_page_html, "html.parser")

top_movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in top_movies]

movies = movie_titles[::-1]

with open("list_top_100_movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")