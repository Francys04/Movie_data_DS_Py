from datetime import datetime
from budget_movies_analysis.procesing_budget import movie_info_list

dates = [movie.get('Release date', 'N/A') for movie in movie_info_list]


def clean_date(date):
    return date.split("(")[0].strip()


def date_convert(date):
    if isinstance(date, list):
        date = date[0]

    if date == "N/A":
        return None
    date_str = clean_date(date)

    fmts = "%B %d %Y", "%d %B %Y"
    for fmt in fmts:
        try:
            return datetime.strftime(date_str, fmt)
        except:
            pass
        return None


for movie in movie_info_list:
    movie['Release date (datetime)'] = date_convert(movie.get('Release date', 'N/A'))

print(movie_info_list[19])

