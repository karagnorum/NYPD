import lib

def n_best_movies(n, data):
    sorted_by_rating = data.sort_values(by=['averageRating'], ascending = False)
    res = sorted_by_rating[['tconst', 'region']].iloc[:n]
    return res

def countries_by_best_movies(data):
    countries_counts = data.groupby(['region']).count()
    res = countries_counts.sort_values(by=['tconst']).index.to_list()
    return res

def analysis1(akas, ratings):
    data = ratings.merge(akas, left_on = ['tconst'], right_index = True)
    best_movies = n_best_movies(200, data)
    for i in range(19):
        order = countries_by_best_movies(best_movies.iloc[:(i+1)*10])
        print(order[:10])
