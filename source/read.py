import pandas as pd
import os

def read_and_cache_akas(read_path, cache_path):

    dtypes = {
        'titleId': 'str',
        'title': 'str',
        'region': 'str',
        'isOriginalTitle': 'int'
    }
    akas = pd.read_csv(read_path, sep='\t', header=0, na_values='\\N', usecols=['titleId', 'title', 'region', 'isOriginalTitle'], dtype=dtypes)
    akas.rename(columns={'titleId': 'tconst'}, inplace=True)

    original_titles = akas[akas['isOriginalTitle'] == 1][['tconst', 'title']]
    akas = akas[akas['isOriginalTitle'] == 0].merge(original_titles, on=['tconst', 'title'])
    counts = akas[['tconst', 'title']].groupby(['tconst']).count()
    movies_with_region_defined = counts.index[counts['title'] == 1].tolist()
    akas.set_index('tconst', inplace=True)
    akas = akas.loc[movies_with_region_defined][['title', 'region']]
    akas.to_csv(cache_path)

    return akas

def read_basics(read_path, cache_path):

    if os.path.exists(cache_path):
        basics = pd.read_csv(cache_path)
    
    else:
        basics_dtypes = {
            'tconst': 'str',
            'startYear': 'float64',
        }

        basics = pd.read_csv(read_path, sep='\t', header=0, na_values='\\N', dtype=basics_dtypes, usecols=['tconst', 'startYear'])
        basics.to_csv(cache_path)

    return basics


def read_frames(paths):

    ratings = pd.read_csv(paths.ratings, sep='\t', header=0, na_values='\\N', dtype={'tconst': 'str', 'averageRating': 'float', 'numVotes': 'int'})

    episodes_dtypes = {
        'tconst': 'str',
        'parentTconst': 'str',
        'seasonNumber': 'float64',
        'episodeNumber': 'float64'
    }

    episodes = pd.read_csv(paths.episodes, sep='\t', header=0, na_values='\\N', dtype=episodes_dtypes)
    episodes.rename(columns={'parentTconst': 'tconst', 'tconst': 'episodeId'}, inplace=True)

    cache_path = 'akas_cache.csv'

    if os.path.exists(cache_path):
        akas = pd.read_csv(cache_path)
        akas.set_index('tconst', inplace=True)
    else:
        akas = read_and_cache_akas(paths.akas, cache_path)

    return [ratings, akas, episodes]
