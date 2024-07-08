import pandas as pd
import matplotlib.pyplot as plt

def analysis3(ratings, episodes):
    
    min_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].min()
    which_series = min_episodes.groupby(['tconst']).apply(lambda x: x.isin([0, 1]).all())
    which_series = which_series.reset_index()
    which_series.columns = ['tconst', 'valid']
    episodes = episodes.merge(which_series, on=['tconst'])
    episodes = episodes.loc[episodes['valid'] == True]

    last_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].max()
    episodes_totals = last_episodes.groupby(['tconst']).sum().reset_index()
    episodes_totals = episodes_totals.merge(ratings, on=['tconst'])

