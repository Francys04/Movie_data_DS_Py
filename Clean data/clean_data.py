import json
from scraping.processing_all_movie import movie_info_list

"""Tasks for this file:
clean uf references
convert running time into a integer
convert dates into datetime obj
split up the long strings
convert budget & box office to numbers"""

# Specify the path to your JSON file
movie_info_list_clean = '../scraping/movie_info.json'

try:
    # Open the JSON file for reading
    with open(movie_info_list_clean, 'r') as json_file:
        # Load the JSON data
        data = json.load(json_file)

        # Print the JSON data
        print(json.dumps(data, indent=4))  # Pretty print with an indentation of 4 spaces
except FileNotFoundError:
    print(f"File not found: {movie_info_list_clean}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")


# 85 minutes

def min_to_int(running_time):
    if running_time == 'N/A':
        return None
    if isinstance(running_time, list):
        return int(running_time[0].split(" ")[0])
    else:
        return int(running_time.split(" ")[0])


for movie in movie_info_list:
    movie['Running time (int)'] = min_to_int(movie.get('Running time', 'N/A'))

print([movie.get('Running time (int)', 'N/A') for movie in movie_info_list])

print(movie_info_list[-11])