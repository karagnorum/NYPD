import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

def analysis3(ratings, episodes):
    
    min_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].min()
    which_series = min_episodes.groupby(['tconst']).apply(lambda x: x.isin([0, 1]).all())
    which_series = which_series.reset_index()
    which_series.columns = ['tconst', 'valid']
    episodes = episodes.merge(which_series, on=['tconst'])
    episodes = episodes.loc[episodes['valid'] == True]

    last_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].max()
    episodes_totals = last_episodes.groupby(['tconst']).sum().reset_index()
    episodes_totals.rename(columns={'episodeNumber': 'numberOfEpisodes'}, inplace=True)
    episodes_totals = episodes_totals.merge(ratings, on=['tconst'])
    
    #remove outliers
    quantile_99 = episodes_totals['numberOfEpisodes'].quantile(0.99)
    episodes_totals = episodes_totals.loc[episodes_totals['numberOfEpisodes'] <= quantile_99]

    avg_rating = episodes_totals['averageRating']
    num_episodes = episodes_totals['numberOfEpisodes']
    print(st.pearsonr(avg_rating, num_episodes).statistic)
    plt.scatter(avg_rating, num_episodes)
    plt.xlabel('average rating')
    plt.ylabel('number of episodes')
    plt.show()

