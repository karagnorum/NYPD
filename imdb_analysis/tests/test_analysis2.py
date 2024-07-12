import pytest
import pandas as pd
from imdb_analysis.task2 import analysis2

# Sample data for testing
data = pd.DataFrame({
    'region': ['US', 'GB', 'FR'],
    'feature': [100, 200, 300]
})

resources = {
    'codes': pd.DataFrame({
        'alpha-2': ['US', 'GB', 'FR'],
        'alpha-3': ['USA', 'GBR', 'FRA']
    }),
    'stat1': pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'FRA'],
        'value': [1.5, 2.5, 3.5]
    }),
    'stat2': pd.DataFrame({
        'alpha-3': ['USA', 'GBR', 'FRA'],
        'value': [30, 20, 10]
    })
}

statistics = ['stat1', 'stat2']

def test_analysis2_basic_case():
    # Define the expected output
    expected_output = {
        'stat1': {'GB', 'US', 'FR'},
        'stat2': {'FR'}
    }
    
    # Call the function
    result = analysis2(data, resources, statistics, 'feature')
    print(result)
    
    # Check the result
    assert result == expected_output

def test_analysis2_missing_statistics():
    result = analysis2(data, resources, [], 'feature')
    expected_output = {}
    
    assert result == expected_output

def test_analysis2_incorrect_feature_column():
    with pytest.raises(KeyError):
        analysis2(data, resources, statistics, 'nonexistent_feature')

def test_analysis2_more_country_codes():

    data = pd.DataFrame({
        'region': ['US', 'GB', 'FR', 'DE'],
        'feature': [100, 200, 300, 400]
    })
    resources = {
        'codes': pd.DataFrame({
            'alpha-2': ['US', 'GB', 'FR', 'DE'],
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU']
        }),
        'stat1': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [2, 1, 3, 4]
        }),
        'stat2': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [4, 3, 1, 2]
        })
    }
    
    result = analysis2(data, resources, statistics, 'feature')
    expected_output = {'stat1': {'GB'}, 'stat2': {'FR', 'DE'}}
    
    assert result == expected_output

statistics = ['stat1', 'stat2']

def test_analysis2_some_hegemons():
    data_all_equal = pd.DataFrame({
        'region': ['US', 'GB', 'FR', 'DE'],
        'feature': [100, 100, 100, 100]
    })

    resources = {
        'codes': pd.DataFrame({
            'alpha-2': ['US', 'GB', 'FR', 'DE'],
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU']
        }),
        'stat1': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [1, 2, 2, 1]
        }),
        'stat2': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [1, 1, 1, 2]
        })
    }

    statistics_all_equal = ['stat1', 'stat2']

    expected_output = {
        'stat1': {'US', 'DE'},
        'stat2': {'US', 'GB', 'FR'}
    }

    result = analysis2(data_all_equal, resources, statistics_all_equal, 'feature')

    assert result == expected_output

def test_analysis2_hegemons():
    data = pd.DataFrame({
        'region': ['US', 'GB', 'FR', 'DE'],
        'feature': [400, 300, 200, 100]
    })

    resources = {
        'codes': pd.DataFrame({
            'alpha-2': ['US', 'GB', 'FR', 'DE'],
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU']
        }),
        'stat1': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [4, 3, 2, 1]
        }),
        'stat2': pd.DataFrame({
            'alpha-3': ['USA', 'GBR', 'FRA', 'DEU'],
            'value': [1, 2, 3, 4]
        })
    }

    expected_output = {
        'stat1': {'US', 'GB', 'FR', 'DE'},
        'stat2': {'US'}
    }

    result = analysis2(data, resources, statistics, 'feature')

    assert result == expected_output