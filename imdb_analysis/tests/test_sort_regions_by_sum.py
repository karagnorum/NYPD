import pytest
import pandas as pd
from imdb_analysis.task2 import sort_regions_by_sum


@pytest.fixture
def sample_data1():
    return pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'UK', 'FR', 'DE'],
        'value': [100, 150, 200, 250]
    })

@pytest.fixture
def sample_data2():
    return pd.DataFrame({
        'tconst': ['tt0000005', 'tt0000006', 'tt0000007', 'tt0000008', 'tt0000009'],
        'region': ['US', 'US', 'UK', 'FR', 'FR'],
        'value': [120, 130, 140, 110, 115]
    })

@pytest.fixture
def sample_data3():
    return pd.DataFrame({
        'tconst': ['tt0000010', 'tt0000011', 'tt0000012', 'tt0000013'],
        'region': ['DE', 'DE', 'US', 'UK'],
        'value': [110, 90, 210, 150]
    })

def test_sort_regions_by_sum_sample_data1(sample_data1):
    result = sort_regions_by_sum(sample_data1, 'value')
    expected = pd.DataFrame({'alpha-2': ['DE', 'FR', 'UK', 'US']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_sample_data2(sample_data2):
    result = sort_regions_by_sum(sample_data2, 'value')
    expected = pd.DataFrame({'alpha-2': ['US', 'FR', 'UK']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_sample_data3(sample_data3):
    result = sort_regions_by_sum(sample_data3, 'value')
    expected = pd.DataFrame({'alpha-2': ['US', 'DE', 'UK']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_combined_data(sample_data1, sample_data2, sample_data3):
    combined_data = pd.concat([sample_data1, sample_data2, sample_data3], ignore_index=True)
    result = sort_regions_by_sum(combined_data, 'value')
    expected = pd.DataFrame({'alpha-2': ['US', 'DE', 'UK', 'FR']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_different_column():
    data = pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'UK', 'FR', 'DE'],
        'other_value': [50, 100, 150, 200]
    })
    result = sort_regions_by_sum(data, 'other_value')
    expected = pd.DataFrame({'alpha-2': ['DE', 'FR', 'UK', 'US']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_single_entry():
    data = pd.DataFrame({
        'tconst': ['tt0000001'],
        'region': ['US'],
        'value': [100]
    })
    result = sort_regions_by_sum(data, 'value')
    expected = pd.DataFrame({'alpha-2': ['US']})
    pd.testing.assert_frame_equal(result, expected)

def test_sort_regions_by_sum_tied_values():
    data = pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'US', 'UK', 'UK'],
        'value': [100, 100, 200, 200]
    })
    result = sort_regions_by_sum(data, 'value')
    expected = pd.DataFrame({'alpha-2': ['UK', 'US']})
    pd.testing.assert_frame_equal(result, expected)
