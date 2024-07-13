def n_best_movies(n, ratings):
    sorted_by_quality = ratings.sort_values(by=['quality'], ascending = False)
    res = sorted_by_quality.iloc[:n]
    return res

def countries_by_best_movies(data):
    countries_counts = data.groupby(['region']).count()
    res = countries_counts.sort_values(by=['tconst'], ascending = False).index.to_list()
    return res

def analysis1(akas, ratings, lst, n):
    ratings_mean = ratings['averageRating'].mean()
    ratings['quality'] = (ratings['averageRating'] - ratings_mean) * ratings['numVotes']

    l = len(lst)
    best_movies = n_best_movies(lst[l-1], ratings.merge(akas, on='tconst'))
    res = [None] * l
    for i in range(l):
        best_of_best_movies = best_movies.iloc[:lst[i]]
        res[i] = countries_by_best_movies(best_of_best_movies)[:n]

    return res


def analysis1_alternative(akas, ratings, lst, n):
    ratings_mean = ratings['averageRating'].mean()
    ratings['quality'] = (ratings['averageRating'] - ratings_mean) * ratings['numVotes']

    l = len(lst)
    best_movies = n_best_movies(lst[l-1], ratings)
    res = [None] * l
    for i in range(l):
        best_of_best_movies = best_movies.iloc[:lst[i]].merge(akas, on='tconst')
        res[i] = countries_by_best_movies(best_of_best_movies)[:n]

    return res
