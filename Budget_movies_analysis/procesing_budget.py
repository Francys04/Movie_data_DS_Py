from clean_data.clean_data import movie_info_list
import re  # This line imports the regular expression (regex) module re, which is used for pattern matching and

# manipulation of strings.

"""This line creates a list comprehension that iterates over the movie_info_list and extracts the 'Budget'
attribute from each movie dictionary using the get method. If 'Budget' is not present in a movie's dictionary, 
it defaults to 'N/A'. The resulting list is printed."""
print([movie.get('Budget', 'N/A') for movie in movie_info_list])

amounts = r"thousand|million|billion"  # It matches the words 'thousand,' 'million,' or 'billion' in a string.
number = r"\d+(,\d{3})*\.*\d*"
standard = fr"\${number}(-|\sto\s)?({number})?\s({amounts})"

"""This line defines a Python function named word_to_value that takes a single argument, word. This function 
is used to convert words like 'thousand,' 'million,' or 'billion' into their corresponding numerical values."""


def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict.get(word.lower(), 1)


"""
This line defines a Python function named parse_word_syntax that takes a single argument, string. 
This function is used to parse and convert strings that use word-based syntax (e.g., "2 million").
"""


def parse_word_syntax(string):
    stripped_string = string.replace(",", "")
    value = float(re.search(number, stripped_string).group())
    modifier = word_to_value(re.search(amounts, string, flags=re.I).group())
    return value * modifier


"""This line defines a Python function named parse_value_syntax that takes a single argument, string. 
This function is used to parse and convert strings that use value-based syntax (e.g., "$2.5 million")."""


def parse_value_syntax(string):
    stripped_string = string.replace(",", "")
    return float(re.search(number, stripped_string).group())


""" This line defines a Python function named money_conversion that takes a single argument, money. 
This function is used to convert monetary values (in various formats) into numerical values."""


def money_conversion(money):
    if type(money) == list:
        money = money[0]

    word_syntax = re.search(standard, money, flags=re.I)
    value_syntax = re.search(fr"\${number}", money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())
    elif value_syntax:
        return parse_value_syntax(value_syntax.group())
    else:
        return None


for movie in movie_info_list:
    movie['Budget (float)'] = money_conversion(movie.get('Budget', 'N/A'))
    movie['Box office (float)'] = money_conversion(movie.get('Box office', 'N/A'))

print(money_conversion(movie_info_list[11]['Budget']))  # Openhimera movie = 12000000.0

# %%
