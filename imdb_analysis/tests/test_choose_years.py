import pytest
import pandas as pd
from imdb_analysis.preparations import choose_years, EmptySubsetChosen

# Fixture to create sample dataframes
@pytest.fixture
def sample_data():
    df = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004', 'tt005'],
        'other_column': ['data1', 'data2', 'data3', 'data4', 'data5']
    })
    
    years = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004', 'tt005'],
        'startYear': [1990, 1995, 2000, 2005, 2010]
    })
    
    return df, years

# Test functions
def test_choose_years_within_range(sample_data):
    df, years = sample_data
    fromYear = 1990
    toYear = 2000
    expected_tconsts = ['tt001', 'tt002', 'tt003']
    
    result_df = choose_years(df, fromYear, toYear, years)
    result_tconsts = result_df['tconst'].tolist()
    
    assert result_tconsts == expected_tconsts

def test_choose_years_single_year(sample_data):
    df, years = sample_data
    fromYear = 2005
    toYear = 2005
    expected_tconsts = ['tt004']
    
    result_df = choose_years(df, fromYear, toYear, years)
    result_tconsts = result_df['tconst'].tolist()
    
    assert result_tconsts == expected_tconsts

def test_choose_years_no_match_raises_exception(sample_data):
    df, years = sample_data
    fromYear = 2015
    toYear = 2020
    
    with pytest.raises(EmptySubsetChosen):
        choose_years(df, fromYear, toYear, years)

def test_choose_years_all_matches(sample_data):
    df, years = sample_data
    fromYear = 1990
    toYear = 2010
    expected_tconsts = ['tt001', 'tt002', 'tt003', 'tt004', 'tt005']
    
    result_df = choose_years(df, fromYear, toYear, years)
    result_tconsts = result_df['tconst'].tolist()
    
    assert result_tconsts == expected_tconsts

def test_choose_years_empty_subset(sample_data):
    df, years = sample_data
    fromYear = 1991
    toYear = 1994
    
    with pytest.raises(EmptySubsetChosen):
        choose_years(df, fromYear, toYear, years)

