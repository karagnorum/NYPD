import pandas as pd

def analysis3(ratings, episodes):
    min_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].min()
    which_series = min_episodes.groupby(['tconst']).apply(lambda x: x.isin([0, 1]).all())
    how_many_invalid = len(which_series[which_series == False])
    msg = 'There were found ' + str(how_many_invalid) + """ series with at least one season  without first episode and were omitted during analysis 3."""
    which_series = which_series.reset_index()
    which_series.columns = ['tconst', 'valid']
    episodes = episodes.merge(which_series, on=['tconst'])
    episodes = episodes.loc[episodes['valid']]

    last_episodes = episodes.groupby(['tconst', 'seasonNumber'])['episodeNumber'].max()
    episodes_totals = last_episodes.groupby(['tconst']).sum().reset_index()
    episodes_totals.rename(columns={'episodeNumber': 'numberOfEpisodes'}, inplace=True)
    episodes_totals = episodes_totals.merge(ratings[['tconst', 'numVotes']], on=['tconst'])
    
    #remove outliers
    quantile_num_epi = episodes_totals['numberOfEpisodes'].quantile(0.99)
    episodes_totals = episodes_totals.loc[episodes_totals['numberOfEpisodes'] <= quantile_num_epi]
    quantile_quality_max = episodes_totals['numVotes'].quantile(0.99)
    episodes_totals = episodes_totals.loc[episodes_totals['numVotes'] <= quantile_quality_max]

    return episodes_totals, msg
    

