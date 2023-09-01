import json
from scraping.processing_all_movie import movie_info_list

json_filename = "movie_info.json"

# Save the movie_info_list to a JSON file
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(movie_info_list, json_file, indent=4)

print(f'Data saved to {json_filename}')

# Load the data from the JSON file
with open(json_filename, 'r', encoding='utf-8') as json_file:
    loaded_movie_info_list = json.load(json_file)

print(f'Data loaded from {json_filename}')