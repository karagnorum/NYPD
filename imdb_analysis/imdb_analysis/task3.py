import pandas as pd

def remove_above_quantile(data, column, which_quantile):
    quantile = data[column].quantile(which_quantile)
    return data.loc[data[column] <= quantile]
    
def analysis3(ratings, episodes, p):
    min_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].min()
    which_series = min_episodes.groupby(['tconst']).apply(lambda x: x.isin([0, 1]).all())
    how_many_invalid = len(which_series[which_series == False])
    msg = 'There were found ' + str(how_many_invalid) + """ series with at least one season without first episode and were omitted during analysis 3."""
    which_series = which_series.reset_index()
    which_series.columns = ['tconst', 'valid']
    episodes = episodes.merge(which_series, on=['tconst'])
    episodes = episodes.loc[episodes['valid']]

    #We assume that number of episodes is a sum of numbers of last episode in each season
    last_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].max()
    episodes_totals = last_episodes.groupby(['tconst']).sum().reset_index()
    episodes_totals.rename(columns={'episodeNumber': 'numberOfEpisodes'}, inplace=True)
    episodes_totals = episodes_totals.merge(ratings[['tconst', 'numVotes']], on=['tconst'])

    #remove outliers
    episodes_totals = remove_above_quantile(episodes_totals, 'numVotes', p)
    episodes_totals = remove_above_quantile(episodes_totals, 'numberOfEpisodes', p)

    return episodes_totals[['numVotes', 'numberOfEpisodes']], msg
    

