from imdb_analysis.task2 import hegemons
import pandas as pd

def test_hegemons_basic():
    statistic_ranks = pd.DataFrame({
        'alpha-2': ['A', 'B', 'C', 'D', 'E'],
        'stat_rank': [1, 2, 3, 4, 5]
    })
    impact_ranks = pd.DataFrame({
        'alpha-2': ['B', 'A', 'D', 'C', 'E'],
        'impact_rank': [1, 2, 3, 4, 5]
    })
    
    expected = {'A', 'C'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_multiple_max_hegemons():
    statistic_ranks = pd.DataFrame({
        'alpha-2': ['A', 'B', 'C', 'E', 'D'],
        'stat_rank': [1, 2, 3, 4, 5]
    })
    impact_ranks = pd.DataFrame({
        'alpha-2': ['E', 'D', 'A', 'C', 'B'],
        'impact_rank': [1, 2, 3, 4, 5]
    })
    
    expected = {'B'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_no_hegemons():
    statistic_ranks = pd.DataFrame({
        'alpha-2': ['A', 'B', 'C', 'D', 'E'],
        'stat_rank': [1, 2, 3, 4, 5]
    })
    impact_ranks = pd.DataFrame({
        'alpha-2': ['A', 'B', 'C', 'D', 'E'],
        'impact_rank': [1, 2, 3, 4, 5]
    })
    
    expected = {'A', 'B', 'C', 'D', 'E'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert sorted(result) == sorted(expected)

def test_hegemons_with_ties():
    statistic_ranks = pd.DataFrame({
        'alpha-2': ['A', 'B', 'C', 'D'],
        'stat_rank': [1, 2, 3, 4]
    })
    impact_ranks = pd.DataFrame({
        'alpha-2': ['D', 'C', 'B', 'A'],
        'impact_rank': [1, 2, 3, 4]
    })
    
    expected = {'A'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert sorted(result) == sorted(expected)

def test_hegemons_single_entry():
    statistic_ranks = pd.DataFrame({
        'alpha-2': ['A'],
        'stat_rank': [1]
    })
    impact_ranks = pd.DataFrame({
        'alpha-2': ['A'],
        'impact_rank': [1]
    })
    
    expected = {'A'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_empty_lists():
    statistic_ranks = pd.DataFrame(columns=['alpha-2', 'stat_rank'])
    impact_ranks = pd.DataFrame(columns=['alpha-2', 'impact_rank'])
    
    expected = set()
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected


# def test_hegemons_basic():
#     statistic_ranks = ['A', 'B', 'C', 'D', 'E']
#     impact_ranks = ['B', 'A', 'D', 'C', 'E']
    
#     expected = {'B', 'D'}
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert result == expected

# def test_hegemons_multiple_max_hegemons():
#     statistic_ranks = ['A', 'B', 'C', 'E', 'D']
#     impact_ranks = ['E', 'D', 'A', 'C', 'B']
    
#     expected = {'E', 'D'}
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert result == expected

# def test_hegemons_no_hegemons():
#     statistic_ranks = ['A', 'B', 'C', 'D', 'E']
#     impact_ranks = ['A', 'B', 'C', 'D', 'E']
    
#     expected = {'A', 'B', 'C', 'D', 'E'}
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert sorted(result) == sorted(expected)

# def test_hegemons_with_ties():
#     statistic_ranks = ['A', 'B', 'C', 'D']
#     impact_ranks = ['D', 'C', 'B', 'A']
    
#     expected = {'D'}
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert sorted(result) == sorted(expected)

# def test_hegemons_single_entry():
#     statistic_ranks = ['A']
#     impact_ranks = ['A']
    
#     expected = {'A'}
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert result == expected

# def test_hegemons_empty_lists():
#     statistic_ranks = []
#     impact_ranks = []
    
#     expected = set()
#     result = hegemons(statistic_ranks, impact_ranks)
    
#     assert result == expected
