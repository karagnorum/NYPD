import pytest
import pandas as pd
from imdb_analysis.task1 import n_best_movies

def n_best_movies(n, data):
    # Sort the data by 'quality' in descending order
    sorted_data = data.sort_values(by='quality', ascending=False)
    # Select the top n movies
    top_n_movies = sorted_data.head(n)
    # Return a subframe with only 'tconst' and 'region' columns
    return top_n_movies[['tconst', 'region']]

@pytest.fixture
def sample_data():
    # Set up a sample dataframe for testing
    return pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'UK', 'FR', 'DE'],
        'quality': [5.5, 8.3, 7.2, 9.0]
    })

def test_n_best_movies_top_2(sample_data):
    result = n_best_movies(2, sample_data)
    expected = pd.DataFrame({
        'tconst': ['tt0000004', 'tt0000002'],
        'region': ['DE', 'UK']
    }).reset_index(drop=True)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_n_best_movies_top_1(sample_data):
    result = n_best_movies(1, sample_data)
    expected = pd.DataFrame({
        'tconst': ['tt0000004'],
        'region': ['DE']
    }).reset_index(drop=True)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_n_best_movies_all(sample_data):
    result = n_best_movies(4, sample_data)
    expected = pd.DataFrame({
        'tconst': ['tt0000004', 'tt0000002', 'tt0000003', 'tt0000001'],
        'region': ['DE', 'UK', 'FR', 'US']
    }).reset_index(drop=True)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_n_best_movies_more_than_available(sample_data):
    result = n_best_movies(10, sample_data)
    expected = pd.DataFrame({
        'tconst': ['tt0000004', 'tt0000002', 'tt0000003', 'tt0000001'],
        'region': ['DE', 'UK', 'FR', 'US']
    }).reset_index(drop=True)
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_n_best_movies_zero(sample_data):
    result = n_best_movies(0, sample_data)
    expected = pd.DataFrame(columns=['tconst', 'region'])
    pd.testing.assert_frame_equal(result, expected)
