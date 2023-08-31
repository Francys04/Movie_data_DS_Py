from bs4 import BeautifulSoup as bs
import requests

'''Load the web page'''

r = requests.get("https://en.wikipedia.org/wiki/Gladiator_(2000_film)")

# Convert to a beautiful soup obj
soup = bs(r.content, features="lxml")

# print out the html
contents = soup.prettify()
# print(contents)


info_box = soup.find(class_="infobox vevent")
# print(info_box.prettify())
info_rows = info_box.find_all("tr")


# for row in info_rows:
# # print(row.prettify())
def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return row_data.get_text().replace("\xa0", " ")


movie_info = {}

for index, row in enumerate(info_rows):
    if index == 0:
        movie_info['title'] = row.find("th").get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find("th").get_text(" ", strip=True)
        content_value = get_content_value(row.find("td"))
        movie_info[content_key] = content_value
print(movie_info)
# {'title': 'Gladiator', 'Directed by': 'Ridley Scott', 'Screenplay by': '\nDavid Franzoni\nJohn Logan\nWilliam ...
