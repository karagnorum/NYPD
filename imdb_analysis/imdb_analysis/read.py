import pandas as pd
import pkg_resources as pk
import os

def get_regions(akas):
    """Assigns a region to each country if it can be unambigously assigned"""
    original_titles = akas[akas['isOriginalTitle'] == 1][['tconst', 'title']]
    akas = akas[akas['isOriginalTitle'] == 0].merge(original_titles, on=['tconst', 
                                                                         'title'])
    counts = akas.groupby(['tconst', 'title']).count()
    counts.reset_index(inplace=True)
    #movies, to which we can unambigously assign a region
    movies_with_region_defined = counts[counts['region'] == 1]['tconst']
    akas = akas.merge(movies_with_region_defined, on='tconst')
    return akas[['tconst', 'region']]

def read_years(read_path):
    """Reads data frame with movies years"""
    basics_dtypes = {
        'tconst': 'str',
        'startYear': 'float64',
    }

    res = pd.read_csv(read_path, sep='\t', header=0, na_values='\\N', dtype=basics_dtypes, usecols=['tconst', 'startYear'], )
    res.dropna(inplace=True)

    return res


def read_frames(paths):
    """Reads ratings, regions and episodes frames"""
    ratings = pd.read_csv(paths.ratings, sep='\t', header=0, na_values='\\N', dtype=
                          {'tconst': 'str', 'averageRating': 'float', 'numVotes': 'int'})

    episodes_dtypes = {
        'tconst': 'str',
        'parentTconst': 'str',
        'seasonNumber': 'float64',
        'episodeNumber': 'float64'
    }
    episodes = pd.read_csv(paths.episodes, sep='\t', header=0, na_values='\\N', 
                           dtype=episodes_dtypes)
    episodes.rename(columns={'parentTconst': 'tconst', 'tconst': 'episodeId'}, 
                    inplace=True)

    dtypes = {
        'titleId': 'str',
        'title': 'str',
        'region': 'str',
        'isOriginalTitle': 'int'
    }
    akas = pd.read_csv(paths.akas, sep='\t', header=0, na_values='\\N', usecols=
                       ['titleId', 'title', 'region', 'isOriginalTitle'], dtype=dtypes)
    akas.rename(columns={'titleId': 'tconst'}, inplace=True)
    regions = get_regions(akas)

    return [ratings, regions, episodes]

def read_resources(statistics):
    """Returns a dictionary od data frames read from additional files needed to perform analysis"""
    res = dict()

    #use pkg_resources to get path independent from where we run the program
    codes_path = pk.resource_filename('imdb_analysis', 'data/codes.csv')
    res['codes'] = pd.read_csv(codes_path, header=0, usecols=['alpha-2', 'alpha-3'])

    for s in statistics:
        #each file with statistic value is named based on statistic
        path = pk.resource_filename('imdb_analysis', 'data/' + s + '.csv')
        df = pd.read_csv(path, header=0, usecols=['Country Code', '2023'])
        res[s] = df.rename(columns={'Country Code': 'alpha-3', '2023': 'value'})
    
    return res
