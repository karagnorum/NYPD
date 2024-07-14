import pandas as pd


def hegemons(statistic_ranks, impact_ranks):
    """Returns set of countries with biggest (impact rank - statistic rank) value"""
    merged = pd.merge(statistic_ranks, impact_ranks, on='alpha-2')
    merged['position_difference'] = merged['impact_rank'] - merged['stat_rank']
    
    max_difference = merged['position_difference'].max()
    res = merged.loc[merged['position_difference'] == max_difference, 'alpha-2'].to_list()
    
    return set(res)

def stat_ranks(statistic, codes, countries):
    """Returns ranks of countries based on value in data frame statistic"""
    res = statistic.dropna()
    #get alpha-3 codes, because they are used in world bank statistics
    res = res.merge(codes, on=['alpha-3'])
    res = res.merge(countries, on = ['alpha-2'])
    res['stat_rank'] = res['value'].rank(method='min').astype('int64')
    return res[['alpha-2', 'stat_rank']]

def rank_by_sum(data, column):
    """Returns ranks of countries based on sum of value in column"""
    sums = data[['region', column]].groupby(['region']).sum().reset_index()
    sums['impact_rank'] = sums[column].rank(method='min').astype('int64')
    sums = sums.rename(columns={'region': 'alpha-2'})
    return sums[['alpha-2', 'impact_rank']]

def analysis2(data, resources, statistics, feature):
    """Returns a dictionary, which assigns each statistic the hegemons as in task 2"""
    #weak impact is sum of votes and strong impact is sum of qualities
    impact_ranks = rank_by_sum(data, feature)
    res = dict()

    #for every statistic, calculate ranks with respect to statistic and find hegemons
    for s in statistics:
        s_ranks = stat_ranks(resources[s], resources['codes'], impact_ranks['alpha-2'])
        res[s] = hegemons(s_ranks, impact_ranks)
    
    return res