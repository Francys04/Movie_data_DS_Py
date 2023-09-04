# Movie Data Processing and Analysis

This Python project focuses on processing and analyzing movie data obtained from various sources, such as Wikipedia. It includes modules for web scraping, data cleaning, and data analysis.
### Purpose:
- The web scraping module is responsible for fetching movie-related data from online sources, specifically Wikipedia pages. It allows the project to collect a wide range of information about movies, such as titles, directors, release dates, and more.
- The project is divided into several parts, each serving a specific purpose.The data analysis module is dedicated to exploring and deriving insights from the cleaned movie data. It includes scripts for generating visualizations, calculating statistical measures, and conducting analyses to answer specific questions about the movie dataset.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Modules](#modules)
    - [Web Scraping](#web-scraping)
    - [Data Cleaning](#data-cleaning)
    - [Data Analysis](#data-analysis)

## Project Overview

This project aims to collect movie-related data from online sources, clean and preprocess the data, and perform various analyses on it. It provides tools to extract information such as movie titles, release dates, budgets, box office earnings, and more.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <https://github.com/Francys04/Movie_data_DS_Py>```


## Modules
### Web Scraping
The web scraping module is responsible for fetching movie data from online sources, such as Wikipedia pages. It utilizes the requests library and Beautiful Soup for parsing HTML content.

1. `processing.py`: Contains functions to scrape movie data from web pages.
processing_all_movie.py: Collects data for a list of movies and stores it in JSON format.
Data Cleaning
The data cleaning module processes raw movie data, converts it into a structured format, and handles various data transformations. It includes functions to convert budget and box office values into numeric formats.

2. `clean_data.py`: Cleans and prepares movie data for analysis.
procesing_budget.py: Converts monetary values into numeric formats.
### Data Analysis
The data analysis module focuses on performing various analyses on the cleaned movie data. It includes scripts for generating insights, visualizations, and statistical measures.

3. `analysis.py`: Analyzes and visualizes movie data.

## Details of Data Conversion
### Running Time Conversion:

#### Purpose: 
- Convert running time from a string (e.g., "145 minutes") to an integer (e.g., 145) representing the number of minutes.
- How: The min_to_int function takes a running time string as input and extracts the numeric portion. It handles cases where running time may be in different formats or units. If the running time is not available ("N/A"), it returns None.
- Example: Input "145 minutes" -> Output 145
### Date Conversion:

#### Purpose: 
- Convert release dates from various string formats (e.g., "January 15 2023," "15 January 2023") into standardized datetime objects for easy date-related calculations.
- How: The clean_date function preprocesses date strings to remove unwanted characters and formats. The date_convert function attempts to parse the date using different date format patterns and returns a datetime object. If the date is not available ("N/A"), it returns None.
- Example: Input "January 15 2023" -> Output Datetime object: 2023-01-15
### Budget and Box Office Conversion:

#### Purpose: 
- Convert budget and box office values from various formats (e.g., "$3 million," "$1.25 billion") into consistent numeric formats (e.g., 3000000, 1250000000).
- How: The money_conversion function handles different syntax patterns, such as "$X million," "$X billion," "$X.Y million," etc. It extracts the numeric value, handles commas and decimals, and converts words like "million" or "billion" into their numerical equivalents.
- Example: Input "$1.25 billion" -> Output 1250000000
### Data Transformation:

#### Purpose: 
- Organize the movie data by adding new fields (e.g., "Running time (int)") or transforming existing fields (e.g., "Budget" to "Budget (float)") to facilitate analysis and visualization.
- How: Iterates through the movie data and applies the conversion functions to relevant fields, storing the transformed data back into the movie data structure.

#### Fig.1 Clean tags
<img src="figures/clean tags.JPG">

#### Fig.2 Date-time of each movie list
<img src="figures/date-time of each movie list.JPG">

#### Fig.3 Show all movie list
<img src="figures/print all movies.JPG">

#### Fig.4 Time of all movies and single movie description budget and time
<img src="figures/time and single film show.JPG">