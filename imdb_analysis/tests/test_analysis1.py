import pytest
import pandas as pd
from imdb_analysis.task1 import analysis1

@pytest.fixture
def sample_data1():
    return pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'DE', 'DE', 'DE'],
        'averageRating': [5.5, 8.3, 7.2, 9.0],
        'numVotes': [100, 150, 200, 250]
    })

@pytest.fixture
def sample_data2():
    return pd.DataFrame({
        'tconst': ['tt0000005', 'tt0000006', 'tt0000007', 'tt0000008', 'tt0000009'],
        'region': ['US', 'US', 'UK', 'FR', 'FR'],
        'averageRating': [7.0, 7.5, 8.0, 6.0, 6.5],
        'numVotes': [100, 50, 20, 300, 200]
    })

@pytest.fixture
def sample_data3():
    return pd.DataFrame({
        'tconst': ['tt0000010', 'tt0000011', 'tt0000012', 'tt0000013'],
        'region': ['DE', 'DE', 'US', 'UK'],
        'averageRating': [9.5, 8.5, 7.5, 6.5],
        'numVotes': [100, 100, 100, 100]
    })
    
import math
    
import math

def lists_almost_equal(lst1, lst2, rel_tol=1e-9, abs_tol=0.0):
    if len(lst1) != len(lst2):
        return False
    return all(math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol) for a, b in zip(lst1, lst2))

def get_ratings(data):
    return data[['tconst', 'averageRating', 'numVotes']]

def get_akas(data):
    return data[['tconst', 'region']]

def test_analysis1_sample_data1(sample_data1):
    ratings = get_ratings(sample_data1)
    result = analysis1(get_akas(sample_data1), ratings, [2, 3], 2)
    print(ratings['quality'])
    assert (result == [['DE'], ['DE']]) and (lists_almost_equal(ratings['quality'].to_list(),  [-200.0, 120.0, -60.0, 375.0]))

def test_analysis1_sample_data2(sample_data2):
    ratings = get_ratings(sample_data2)
    result = analysis1(get_akas(sample_data2), ratings, [1, 2, 3], 2)
    print(ratings['quality'])
    assert (result[0] == ['US']) and (set(result[1]) == {'UK', 'US'}) and (result[2] == ['US', 'UK']) and (ratings['quality'].to_list() == [0.0, 25.0, 20.0, -300.0, -100])

def test_analysis1_sample_data3(sample_data3):
    ratings =  get_ratings(sample_data3)
    result = analysis1(get_akas(sample_data3), ratings, [2, 3, 4], 4)
    print(ratings['quality'])
    assert (result == [['DE'], ['DE', 'US'], ['DE', 'US', 'UK']]) or (result == [['DE'], ['DE', 'US'], ['DE', 'UK', 'US']]) and (ratings['quality'].to_list() == [150.0, 50.0, -50.0, -150.0])
