from bs4 import BeautifulSoup as bs
import requests


# print all movies from table of Universal Pictures

# get all data from Universal Pictures Wiki
def get_content_value(row_data):
    if row_data.find("li"):
        return [li.get_text(" ", strip=True).replace("\xa0", " ") for li in row_data.find_all("li")]
    else:
        return row_data.get_text().replace("\xa0", " ")


def get_info_box(url):
    r = requests.get(url)
    # Convert to a beautiful soup obj
    soup = bs(r.content, features="lxml")
    # print out the html
    # contents = soup.prettify()
    # print(contents)
    info_box = soup.find(class_="infobox vevent")
    # print(info_box.prettify())
    info_rows = info_box.find_all("tr")

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
    return movie_info


'''
# for all movies'''
r1 = requests.get("https://en.wikipedia.org/wiki/Universal_Pictures")

# Convert to a beautiful soup obj
soup1 = bs(r1.content, features="lxml")

movies = soup1.select(".wikitable.sortable i a")
# print(movies[0:10])
# print(len(movies))  # 148 movies

base_path = "https://en.wikipedia.org/"

movie_info_list = []

for index, movie in enumerate(movies):
    if index == 147:
        break
    try:
        relative_path = movie['href']
        full_path = base_path + relative_path
        title = movie['title']

        movie_info_list.append(get_info_box(full_path))

    except Exception as e:
        print(movie.get_text())
        print(e)
print(len(movie_info_list))

