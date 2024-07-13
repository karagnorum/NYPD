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

def ratings(data):
    return data[['tconst', 'averageRating', 'numVotes']]

def akas(data):
    return data[['tconst', 'region']]

def test_analysis1_sample_data1(sample_data1):
    result = analysis1(akas(sample_data1), ratings(sample_data1), [2, 3], 2)
    assert result == [['DE'], ['DE']]

def test_analysis1_sample_data2(sample_data2):
    result = analysis1(akas(sample_data2), ratings(sample_data2), [1, 2, 3], 2)
    assert (result[0] == ['US']) and (set(result[1]) == {'UK', 'US'}) and (result[2] == ['US', 'UK'])

def test_analysis1_sample_data3(sample_data3):
    result = analysis1(akas(sample_data3), ratings(sample_data3), [2, 3, 4], 4)
    assert (result == [['DE'], ['DE', 'US'], ['DE', 'US', 'UK']]) or (result == [['DE'], ['DE', 'US'], ['DE', 'UK', 'US']])
