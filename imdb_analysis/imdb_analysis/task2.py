import pandas as pd
import pkg_resources as pk

def read_world_bank_statistic(path):
    return pd.read_csv(path, header=0, usecols=['Country Code', '2023'])

def get_ranks(path, codes, countries):
    return ranks(read_world_bank_statistic(path), codes, countries)

def ranks(df, codes, countries):
    res = df.rename(columns={'Country Code': 'alpha-3', '2023': 'value'})
    res = res.dropna()
    res = res.merge(codes, on=['alpha-3'])
    res = res.merge(countries, on = ['alpha-2'])
    res = res.sort_values(by=['value'], ascending=False)['alpha-2'].to_list()
    return res

def hegemons(statistic_ranks, impact_ranks):

    df1 = pd.DataFrame({'country': statistic_ranks, 'stat_rank': list(range(len(statistic_ranks)))[::-1]})
    df2 = pd.DataFrame({'country': impact_ranks, 'impact_rank': list(range(len(impact_ranks)))[::-1]})
    
    merged = pd.merge(df1, df2, on='country')
    
    # Calculate the difference between the positions
    merged['position_difference'] = merged['impact_rank'] - merged['stat_rank']
    
    # Find the elements with the maximum position difference
    max_difference = merged['position_difference'].max()
    res = merged.loc[merged['position_difference'] == max_difference, 'country'].to_list()
    
    return res

def analysis2(data):

    codes_path = pk.resource_filename('imdb_analysis', 'data/codes.csv')
    country_codes = pd.read_csv(codes_path, header=0, usecols=['alpha-2', 'alpha-3'])

    sums_of_votes = data[['region', 'numVotes']].groupby(['region']).sum()
    sums_of_votes.sort_values(by = ['numVotes'], ascending = False, inplace = True)
    weak_ranks = pd.DataFrame({'alpha-2': sums_of_votes.index.to_list()})

    strong_impacts = data[['region', 'quality']].groupby(['region']).sum()
    strong_impacts.sort_values(by = ['quality'], ascending = False, inplace = True)
    strong_ranks = pd.DataFrame({'alpha-2': strong_impacts.index.to_list()})

    get_path = lambda s: pk.resource_filename('imdb_analysis', 'data/' + s + '.csv')
    statistics = ['gdp', 'gdp_pc', 'population']
    stat_ranks = dict()
    for s in statistics:
        stat_ranks[s] = get_ranks(get_path(s), country_codes, weak_ranks)
    
    weak_hegemons = dict()
    strong_hegemons = dict()
    for s in statistics:
        weak_hegemons[s] = hegemons(stat_ranks[s], weak_ranks['alpha-2'].to_list())
        strong_hegemons[s] = hegemons(stat_ranks[s], strong_ranks['alpha-2'].tolist())
    
    print('weak impact: ', weak_hegemons)
    print('strong impact: ', strong_hegemons)