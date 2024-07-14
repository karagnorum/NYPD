import pandas as pd
from imdb_analysis.task2 import stat_ranks
from lib import assert_almost_equal

def test_ranks_basic():
    df = pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA'],
        'value': [10, 20, 15, 30, None]
    })
    codes = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR'],
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA']
    })
    countries = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR']
    })
    
    expected = pd.DataFrame({
        'alpha-2': ['US', 'CA', 'GB', 'AU'],
        'stat_rank': [1, 2, 3, 4]
    })
    result = stat_ranks(df, codes, countries)
    
    assert_almost_equal(result, expected)

def test_ranks_with_missing_values():
    df = pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA', 'GER'],
        'value': [10, 20, None, 30, None, 25]
    })
    codes = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR', 'DE'],
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA', 'GER']
    })
    countries = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR', 'DE']
    })
    
    expected = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'DE', 'AU'],
        'stat_rank': [1, 2, 3, 4]
    })
    result = stat_ranks(df, codes, countries)
    
    assert_almost_equal(result, expected)

def test_ranks_with_unlisted_countries():
    df = pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA'],
        'value': [10, 20, 15, 30, 5]
    })
    codes = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR'],
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA']
    })
    countries = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'AU']
    })
    
    expected = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'AU'],
        'stat_rank': [1, 2, 3]
    })
    result = stat_ranks(df, codes, countries)
    
    assert_almost_equal(result, expected)

def test_ranks_all_missing_values():
    df = pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA'],
        'value': [None, None, None, None, None]
    })
    codes = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR'],
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA']
    })
    countries = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR']
    })
    
    expected = pd.DataFrame({
        'alpha-2': [],
        'stat_rank': []
    })
    result = stat_ranks(df, codes, countries)
    
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)

def test_ranks_no_valid_countries():
    df = pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA'],
        'value': [10, 20, 15, 30, 5]
    })
    codes = pd.DataFrame({
        'alpha-2': ['US', 'GB', 'CA', 'AU', 'FR'],
        'alpha-3': ['USA', 'GBR', 'CAN', 'AUS', 'FRA']
    })
    countries = pd.DataFrame({
        'alpha-2': ['JP', 'CN', 'RU']
    })
    
    expected = pd.DataFrame({
        'alpha-2': [],
        'stat_rank': []
    })
    result = stat_ranks(df, codes, countries)
    
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)
