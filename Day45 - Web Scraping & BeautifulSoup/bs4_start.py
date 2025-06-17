# from bs4 import BeautifulSoup
# import requests
# from pprint import pprint
# import lxml --> some sites demand lmxl parser in the "features" arg

# with open("website.html") as web_file:
#     contents = web_file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # Search all <tag>s
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1",  id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print (section_heading.get("class"))
#
# # Select a specific <tag>
#
# # company_url = soup.select_one(selector="p a") # --> Tag path
# # company_url = soup.select_one(selector="#name") # --> id
# company_url = soup.select(selector=".heading") # --> class
# # print(company_url)



# Scrapping main hacker news website


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Seleciona os 30 primeiros <a> dentro de span.titleline
article_tags = soup.select("span.titleline > a")[:30]
subtexts = soup.select("td.subtext")[:30]

titles = []
links = []
scores = []

for i in range(30):
    article = article_tags[i]
    subtext = subtexts[i]

    # Apenas o texto da <a> (sem domínio)
    titles.append(article.get_text(strip=True))

    # Apenas o href da <a>
    links.append(article.get("href"))

    # Upvotes
    score_tag = subtext.find(class_="score")
    if score_tag:
        score = int(score_tag.get_text().replace(" points", ""))
    else:
        score = 0
    scores.append(score)

# Imprime os resultados
# for i in range(30):
#     print(f"{i+1}. {titles[i]} ({scores[i]} pontos)")
#     print(f"   Link: {links[i]}")

max_upvote = 0
for i in range(0,len(scores)-1):
    if scores[i] > max_upvote:
        max_upvote = scores[i]
max_upvote_index = scores.index(max_upvote)

print(max_upvote)
print(f"The most voted article was '{titles[max_upvote_index]}' ({scores[max_upvote_index]} pontos)")
print(f"Link: {links[max_upvote_index]}")