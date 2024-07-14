import pytest
from imdb_analysis.task1 import countries_by_best_movies
import pandas as pd

@pytest.fixture
def sample_data():
    # Set up a sample dataframe for testing
    return pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004', 'tt0000005'],
        'region': ['US', 'UK', 'FR', 'UK', 'US'],
        'quality': [5.5, 8.3, 7.2, 9.0, 6.0]
    })

def test_countries_by_best_movies(sample_data):
    result = countries_by_best_movies(sample_data)
    assert (set(result[0:2]) == {'US', 'UK'}) and result[2] == 'FR'

def test_countries_by_best_movies_single_entry():
    data = pd.DataFrame({
        'tconst': ['tt0000001'],
        'region': ['US'],
        'quality': [5.5]
    })
    result = countries_by_best_movies(data)
    expected = ['US']
    assert result == expected

def test_countries_by_best_movies_no_entries():
    data = pd.DataFrame(columns=['tconst', 'region', 'quality'])
    result = countries_by_best_movies(data)
    expected = []
    assert result == expected

def test_countries_by_best_movies2():
    data = pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'GB', 'US', 'UK'],
        'quality': [5.5, 8.3, 7.2, 9.0]
    })
    result = countries_by_best_movies(data)
    assert result[0] == 'US' and set(result) == set(data['region'])