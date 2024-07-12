from imdb_analysis.task2 import hegemons

def test_hegemons_basic():
    statistic_ranks = ['A', 'B', 'C', 'D', 'E']
    impact_ranks = ['B', 'A', 'D', 'C', 'E']
    
    expected = {'B', 'D'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_multiple_max_hegemons():
    statistic_ranks = ['A', 'B', 'C', 'E', 'D']
    impact_ranks = ['E', 'D', 'A', 'C', 'B']
    
    expected = {'E', 'D'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_no_hegemons():
    statistic_ranks = ['A', 'B', 'C', 'D', 'E']
    impact_ranks = ['A', 'B', 'C', 'D', 'E']
    
    expected = {'A', 'B', 'C', 'D', 'E'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert sorted(result) == sorted(expected)

def test_hegemons_with_ties():
    statistic_ranks = ['A', 'B', 'C', 'D']
    impact_ranks = ['D', 'C', 'B', 'A']
    
    expected = {'D'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert sorted(result) == sorted(expected)

def test_hegemons_single_entry():
    statistic_ranks = ['A']
    impact_ranks = ['A']
    
    expected = {'A'}
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected

def test_hegemons_empty_lists():
    statistic_ranks = []
    impact_ranks = []
    
    expected = set()
    result = hegemons(statistic_ranks, impact_ranks)
    
    assert result == expected
