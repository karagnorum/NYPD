import pandas as pd
import pytest
from imdb_analysis.read import filter_akas
from lib import assert_almost_equal

data1 = {
    'tconst': ['tt0000001', 'tt0000002', 'tt0000001', 'tt0000002'],
    'title': ['Przypadek', 'Przypadek', 'Przypadek', 'Przypadek'],
    'isOriginalTitle': [1, 0, 0, 1],
    'region': [None, 'PL', 'PL', None]
}
expected_data1 = {
    'tconst': ['tt0000001', 'tt0000002', ],
    'region': ['PL', 'PL', ]
}

data2 = {
    'tconst': ['tt0000005', 'tt0000005', 'tt0000006', 'tt0000006'],
    'title': ['Title A', 'Title A', 'Title B', 'Title B'],
    'isOriginalTitle': [1, 0, 1, 0],
    'region': [None, 'US', None, 'PL']
}
expected_data2 = {
    'tconst': ['tt0000005', 'tt0000006'],
    'region': ['US', 'PL']
}

data3 = {
    'tconst': ['tt0000008', 'tt0000008', 'tt0000008', 'tt0000009', 'tt0000009'],
    'title': ['Movie X', 'Movie X', 'Movie X', 'Movie Y', 'Movie Y'],
    'isOriginalTitle': [1, 0, 0, 1, 0],
    'region': [None, 'FR', 'US', None, 'JP']
}
expected_data3 = {
    'tconst': ['tt0000009'],
    'region': ['JP']
}

data4 = {
    'tconst': ['tt0000008', 'tt0000008', 'tt0000008', 'tt0000009', 'tt0000009'],
    'title': ['Movie X', 'Movie X', 'Movie X', 'Movie X', 'Movie X'],
    'isOriginalTitle': [1, 0, 0, 1, 0],
    'region': [None, 'FR', 'US', None, 'JP']
}
expected_data4 = {
    'tconst': ['tt0000009'],
    'region': ['JP']
}


data5 = {
    'tconst': ['tt0000008', 'tt0000008', 'tt0000008', 'tt0000009', 'tt0000009','tt0000009'],
    'title': ['Movie X', 'Movie X', 'Movie X', 'Movie X', 'Movie X', 'Movie X'],
    'isOriginalTitle': [1, 0, 0, 1, 0, 0],
    'region': [None, 'FR', 'US', None, 'JP', 'US']
}
expected_data5 = {
    'tconst': [],
    'region': []
}

def run_test(data, expected_data):
    akas = pd.DataFrame(data)
    expected_df = pd.DataFrame(expected_data)
    result_df = filter_akas(akas)
    print(result_df)
    assert_almost_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_filter_akas_dataset1():
    run_test(data1, expected_data1)

def test_filter_akas_dataset2():
    run_test(data2, expected_data2)

def test_filter_akas_dataset3():
    run_test(data3, expected_data3)

def test_filter_akas_dataset4():
    run_test(data4, expected_data4)

def test_filter_akas_dataset5():
    run_test(data5, expected_data5)