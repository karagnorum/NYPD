import pandas as pd
import pkg_resources as pk
import os

def filter_akas(akas):
    original_titles = akas[akas['isOriginalTitle'] == 1][['tconst', 'title']]
    akas = akas[akas['isOriginalTitle'] == 0].merge(original_titles, on=['tconst', 'title'])
    counts = akas.groupby(['tconst', 'title']).count()
    counts.reset_index(inplace=True)
    movies_with_region_defined = counts[counts['region'] == 1]['tconst']
    akas = akas.merge(movies_with_region_defined, on='tconst')
    return akas[['tconst', 'region']]

def read_and_cache_akas(read_path, cache_path):

    dtypes = {
        'titleId': 'str',
        'title': 'str',
        'region': 'str',
        'isOriginalTitle': 'int'
    }
    akas = pd.read_csv(read_path, sep='\t', header=0, na_values='\\N', usecols=['titleId', 'title', 'region', 'isOriginalTitle'], dtype=dtypes, )
    akas.rename(columns={'titleId': 'tconst'}, inplace=True)
    akas = filter_akas(akas)
    akas.to_csv(cache_path)

    return akas

def read_years(read_path, cache_path):

    if os.path.exists(cache_path):
        basics = pd.read_csv(cache_path, usecols=['tconst', 'startYear'])
    
    else:
        basics_dtypes = {
            'tconst': 'str',
            'startYear': 'float64',
        }

        basics = pd.read_csv(read_path, sep='\t', header=0, na_values='\\N', dtype=basics_dtypes, usecols=['tconst', 'startYear'], )
        basics.dropna(inplace=True)
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

    episodes = pd.read_csv(paths.episodes, sep='\t', header=0, na_values='\\N', dtype=episodes_dtypes, )
    episodes.rename(columns={'parentTconst': 'tconst', 'tconst': 'episodeId'}, inplace=True)

    cache_path = 'akas_cache.csv'

    if os.path.exists(cache_path):
        akas = pd.read_csv(cache_path)
    else:
        akas = read_and_cache_akas(paths.akas, cache_path)

    return [ratings, akas, episodes]

def read_resources(statistics):
    res = dict()

    codes_path = pk.resource_filename('imdb_analysis', 'data/codes.csv')
    res['codes'] = pd.read_csv(codes_path, header=0, usecols=['alpha-2', 'alpha-3'])

    for s in statistics:
        path = pk.resource_filename('imdb_analysis', 'data/' + s + '.csv')
        df = pd.read_csv(path, header=0, usecols=['Country Code', '2023'])
        res[s] = df.rename(columns={'Country Code': 'alpha-3', '2023': 'value'})
    
    return res
