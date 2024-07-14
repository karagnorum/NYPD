import pytest
import pandas as pd
from imdb_analysis.task2 import rank_by_sum

import pytest
import pandas as pd
from imdb_analysis.task2 import rank_by_sum
from lib import assert_almost_equal

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
    result = rank_by_sum(sample_data1, 'value')
    expected = pd.DataFrame({
        'alpha-2': ['US', 'UK', 'FR', 'DE'],
        'impact_rank': [1, 2, 3, 4]
    })
    assert_almost_equal(result, expected)

def test_sort_regions_by_sum_sample_data2(sample_data2):
    result = rank_by_sum(sample_data2, 'value')
    expected = pd.DataFrame({
        'alpha-2': ['UK', 'FR', 'US'],
        'impact_rank': [1, 2, 3]
    })
    assert_almost_equal(result, expected)

def test_sort_regions_by_sum_sample_data3(sample_data3):
    result = rank_by_sum(sample_data3, 'value')
    expected = pd.DataFrame({
        'alpha-2': ['UK', 'DE', 'US'],
        'impact_rank': [1, 2, 3]
    })
    assert_almost_equal(result, expected)

def test_sort_regions_by_sum_different_column():
    data = pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'UK', 'FR', 'DE'],
        'other_value': [50, 100, 150, 200]
    })
    result = rank_by_sum(data, 'other_value')
    expected = pd.DataFrame({
        'alpha-2': ['US', 'UK', 'FR', 'DE'],
        'impact_rank': [1, 2, 3, 4]
    })
    assert_almost_equal(result, expected)

def test_sort_regions_by_sum_single_entry():
    data = pd.DataFrame({
        'tconst': ['tt0000001'],
        'region': ['US'],
        'value': [100]
    })
    result = rank_by_sum(data, 'value')
    expected = pd.DataFrame({
        'alpha-2': ['US'],
        'impact_rank': [1]
    })
    assert_almost_equal(result, expected)

def test_sort_regions_by_sum_tied_values():
    data = pd.DataFrame({
        'tconst': ['tt0000001', 'tt0000002', 'tt0000003', 'tt0000004'],
        'region': ['US', 'US', 'UK', 'UK'],
        'value': [100, 100, 200, 200]
    })
    result = rank_by_sum(data, 'value')
    expected = pd.DataFrame({
        'alpha-2': ['US', 'UK'],
        'impact_rank': [1, 2]
    })
    assert_almost_equal(result, expected)
