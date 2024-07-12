import pandas as pd


def hegemons(statistic_ranks, impact_ranks):
    merged = pd.merge(statistic_ranks, impact_ranks, on='alpha-2')
    merged['position_difference'] = merged['impact_rank'] - merged['stat_rank']
    
    max_difference = merged['position_difference'].max()
    res = merged.loc[merged['position_difference'] == max_difference, 'alpha-2'].to_list()
    
    return set(res)

def get_stat_ranks(df, codes, countries):
    res = df.dropna()
    res = res.merge(codes, on=['alpha-3'])
    res = res.merge(countries, on = ['alpha-2'])
    res['stat_rank'] = res['value'].rank(method='min', ascending = False)
    return res[['alpha-2', 'stat_rank']]

def rank_by_sum(data, column):
    sums = data[['region', column]].groupby(['region']).sum().reset_index()
    sums['impact_rank'] = sums[column].rank(method='min', ascending = False)
    sums = sums.rename(columns={'region': 'alpha-2'})
    return sums[['alpha-2', 'impact_rank']]

def analysis2(data, resources, statistics, feature):
    impact_ranks = rank_by_sum(data, feature)
    print(impact_ranks)
    res = dict()

    for s in statistics:
        s_ranks = get_stat_ranks(resources[s], resources['codes'], impact_ranks['alpha-2'])
        res[s] = hegemons(s_ranks, impact_ranks)
    
    return res