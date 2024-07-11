import pandas as pd
import pkg_resources as pk


def hegemons(statistic_ranks, impact_ranks):
    df1 = pd.DataFrame({'country': statistic_ranks, 'stat_rank': list(range(len(statistic_ranks)))[::-1]})
    df2 = pd.DataFrame({'country': impact_ranks, 'impact_rank': list(range(len(impact_ranks)))[::-1]})
    
    merged = pd.merge(df1, df2, on='country')
    merged['position_difference'] = merged['impact_rank'] - merged['stat_rank']
    
    max_difference = merged['position_difference'].max()
    res = merged.loc[merged['position_difference'] == max_difference, 'country'].to_list()
    
    return res

def ranks(df, codes, countries):
    res = df.rename(columns={'Country Code': 'alpha-3', '2023': 'value'})
    res = res.dropna()
    res = res.merge(codes, on=['alpha-3'])
    res = res.merge(pd.DataFrame({'alpha-2': countries}), on = ['alpha-2'])
    res = res.sort_values(by=['value'], ascending=False)['alpha-2'].to_list()
    return res

def statistic_ranks(statistic, codes, countries):
    path = pk.resource_filename('imdb_analysis', 'data/' + statistic + '.csv')
    df = pd.read_csv(path, header=0, usecols=['Country Code', '2023'])
    return ranks(df, codes, countries)

def sort_regions_by_sum(data, feature):
    sums = data[['region', feature]].groupby(['region']).sum()
    sums.sort_values(by = [feature], ascending = False, inplace = True)
    return pd.DataFrame(sums.index.to_list())

def analysis2(data):

    codes_path = pk.resource_filename('imdb_analysis', 'data/codes.csv')
    country_codes = pd.read_csv(codes_path, header=0, usecols=['alpha-2', 'alpha-3'])

    weak_ranks = sort_regions_by_sum(data, 'numVotes')
    strong_ranks = sort_regions_by_sum(data, 'quality')

    weak_hegemons = dict()
    strong_hegemons = dict()
    for s in ['gdp', 'gdp_pc', 'population']:
        s_ranks = statistic_ranks(s, country_codes, weak_ranks)
        weak_hegemons[s] = hegemons(s_ranks, weak_ranks)
        strong_hegemons[s] = hegemons(s_ranks, strong_ranks)
    
    print('weak impact: ', weak_hegemons)
    print('strong impact: ', strong_hegemons)