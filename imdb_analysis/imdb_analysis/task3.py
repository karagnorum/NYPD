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
    episodes_totals.rename(columns={'episodeNumber': 'numberOfEpisodes'}, inplace=True)
    episodes_totals = episodes_totals.merge(ratings[['tconst', 'numVotes']], on=['tconst'])
    
    #remove outliers
    quantile_num_epi = episodes_totals['numberOfEpisodes'].quantile(0.99)
    episodes_totals = episodes_totals.loc[episodes_totals['numberOfEpisodes'] <= quantile_num_epi]
    quantile_quality_max = episodes_totals['numVotes'].quantile(0.99)
    episodes_totals = episodes_totals.loc[episodes_totals['numVotes'] <= quantile_quality_max]

    avg_rating = episodes_totals['numVotes']
    num_episodes = episodes_totals['numberOfEpisodes']
    plt.scatter(avg_rating, num_episodes, s = 1)
    plt.xlabel('numVotes')
    plt.ylabel('number of episodes')
    plt.show()

