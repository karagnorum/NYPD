def n_best_movies(n, data):
    sorted_by_quality = data.sort_values(by=['quality'], ascending = False)
    res = sorted_by_quality[['tconst', 'region']].iloc[:n]
    return res

def countries_by_best_movies(data):
    countries_counts = data.groupby(['region']).count()
    res = countries_counts.sort_values(by=['tconst'], ascending = False).index.to_list()
    return res

def analysis1(data, lst, n):
    average_rating = data['averageRating'].mean()
    data['quality'] = (data['averageRating'] - average_rating) * data['numVotes']

    l = len(lst)
    best_movies = n_best_movies(lst[l-1], data)
    res = [None] * l
    for i in range(l):
        order = countries_by_best_movies(best_movies.iloc[:lst[i]])
        res[i] = order[:n]

    return res
