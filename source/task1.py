import lib

def n_best_movies(n, ratings):
    ratings_sorted = ratings.sort_values(by=['averageRating'], ascending = False)
    res = ratings_sorted['tconst'][:200].to_list()
    return res

def countries_by_best_movies(akas, best_movies):
    
    print(akas.index)
    res = akas.loc[best_movies].groupby(['region']).count()

def analysis1(akas, ratings):

    original_titles = akas[akas['isOriginalTitle'] == 1][['tconst', 'title']]
    akas = akas[akas['isOriginalTitle'] == 0].merge(original_titles, on=['tconst', 'title'])
    counts = akas[['tconst', 'title']].groupby(['tconst']).count()
    movies_with_region_defined = counts.index[counts['title'] == 1].tolist()

    akas = akas.set_index('tconst')
    akas = akas.loc[movies_with_region_defined]

    best_movies = [None] * 20
    best_movies[19] = n_best_movies(200, ratings)
    for i in range(19):
        best_movies[i] = best_movies[19][:(i+1)*10]

    for i in range(19):
        order = countries_by_best_movies(akas, best_movies[i])
        # print(order[:10])