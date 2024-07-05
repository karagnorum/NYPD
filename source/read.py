import pandas as pd
import os


def read_frames(paths):
    
    #delete nrows
    ratings = pd.read_csv(paths.ratings, sep='\t', header=0, na_values='\\N', dtype= {'tconst': 'str', 'averageRating': 'float', 'numVotes': 'int'}, nrows=500)

    dtypes = {
        'titleId': 'str',
        'ordering': 'int',
        'title': 'str',
        'region': 'str',
        'language': 'str',
        'types': 'str',
        'attributes': 'str',
        'isOriginalTitle': 'int'
    }

    akas = pd.read_csv(paths.akas, sep='\t', header=0, na_values='\\N', dtype=dtypes, nrows=100)
    akas.rename(columns={'titleId': 'tconst'}, inplace=True)

    # Define the data types for each column
    basics_dtypes = {
        'tconst': 'str',
        'titleType': 'str',
        'primaryTitle': 'str',
        'originalTitle': 'str',
        'isAdult': 'int64',
        'startYear': 'float64',
        'endYear': 'float64',  
        'runtimeMinutes': 'float64',
        'genres': 'object'
    }
    basics = pd.read_csv(paths.basics, sep='\t', header=0, na_values='\\N', dtype=basics_dtypes, nrows=100)

    # Define the data types for each column
    episodes_dtypes = {
        'tconst': 'str',
        'parentTconst': 'str',
        'seasonNumber': 'float64', 
        'episodeNumber': 'float64' 
    }
    episodes = pd.read_csv(paths.episodes, sep='\t', header=0, na_values='\\N', dtype=episodes_dtypes, nrows=100)
    episodes.rename(columns={'parentTconst': 'tconst', 'tconst': 'episodeId'}, inplace=True)

    return [ratings, akas, basics, episodes]



