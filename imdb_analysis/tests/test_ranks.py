import pandas as pd
from imdb_analysis.task2 import ranks

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
    
    expected = (['AU', 'GB', 'CA', 'US'])
    result = ranks(df, codes, countries)
    
    result == expected

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
    
    expected = (['AU', 'DE', 'GB', 'US'])
    result = ranks(df, codes, countries)
    
    result == expected

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
    
    expected = (['AU', 'GB', 'US'])
    result = ranks(df, codes, countries)
    
    result == expected

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
    
    expected = []
    result = ranks(df, codes, countries)
    
    result == expected

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
    
    expected = []
    result = ranks(df, codes, countries)
    
    result == expected

