from datetime import datetime  # This line imports the datetime class from the datetime module,
# which is used to work with date and time data in Python.
from budget_movies_analysis.procesing_budget import movie_info_list

"""This line creates a list called dates using a list comprehension. It extracts the 'Release date' values from each 
movie in the movie_info_list. If the 'Release date' is not available ('N/A'), it uses the default value 'N/A'."""
dates = [movie.get('Release date', 'N/A') for movie in movie_info_list]

"""This line defines a Python function named clean_date. It takes one argument, date, which represents a date string."""


def clean_date(date):
    return date.split("(")[0].strip()


'''This line defines a tuple of date format strings. It specifies two possible date formats:

%B %d %Y: Full month name, day of the month, and year (e.g., "January 15 2023").
%d %B %Y: Day of the month, full month name, and year (e.g., "15 January 2023").'''


def date_convert(date):
    if isinstance(date, list):  # This line checks if date is a list. In some cases, dates may be provided as a
        # list of different formats or versions.
        date = date[0]

    if date == "N/A":
        return None
    date_str = clean_date(date)

    fmts = "%B %d %Y", "%d %B %Y"
    for fmt in fmts:
        try:
            return datetime.strftime(date_str, fmt)
        except:  # This line specifies the except block, which is executed if an exception occurs during the
            # conversion attempt.
            pass
        return None


for movie in movie_info_list:
    movie['Release date (datetime)'] = date_convert(movie.get('Release date', 'N/A'))

print(movie_info_list[19])
