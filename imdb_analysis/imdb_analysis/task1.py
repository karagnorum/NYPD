def n_best_movies(n, data):
    sorted_by_rating = data.sort_values(by=['quality'], ascending = False)
    res = sorted_by_rating[['tconst', 'region']].iloc[:n]
    return res

def countries_by_best_movies(data):
    countries_counts = data.groupby(['region']).count()
    res = countries_counts.sort_values(by=['tconst']).index.to_list()
    return res

def analysis1(akas, ratings):
    data = ratings.merge(akas, on = ['tconst'])
    average_rating = data['averageRating'].mean()
    data['quality'] = (data['averageRating'] - average_rating) * data['numVotes']

    best_movies = n_best_movies(200, data)
    for i in range(20):
        order = countries_by_best_movies(best_movies.iloc[:(i+1)*10])
        print(f'countries with most movies among {(i+1)*10} best movies: {order[:10]}')

    return data
