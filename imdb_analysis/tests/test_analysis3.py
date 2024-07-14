from imdb_analysis.task3 import analysis3
import pandas as pd
from lib import assert_almost_equal


def test_analysis3_valid_input():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003'],
        'averageRating': [7.5, 8.0, 9.0],
        'numVotes': [100, 150, 200]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005', 'ep006', 'ep007'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt002', 'tt003', 'tt003'],
        'seasonNumber': [1, 1, 1, 1, 2, 1, 2],
        'episodeNumber': [0, 1, 0, 1, 1, 0, 1]
    })

    p = 1

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame({
        'numVotes': [100, 150, 200],
        'numberOfEpisodes': [1, 2, 1],
    })

    assert msg == 'There were found 0 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_analysis3_quantile_filter():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004'],
        'averageRating': [7.5, 8.0, 9.0, 7.8],
        'numVotes': [100, 150, 200, 50]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005', 'ep006', 'ep007', 'ep008'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt002', 'tt003', 'tt003', 'tt004'],
        'seasonNumber': [1, 1, 1, 1, 2, 1, 2, 1],
        'episodeNumber': [0, 1, 0, 1, 1, 0, 1, 0]
    })

    p = 0.5

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame({
        'numVotes': [50],
        'numberOfEpisodes': [0],
    })

    assert msg == 'There were found 0 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_analysis3_all_valid_series():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003'],
        'averageRating': [7.5, 8.0, 9.0],
        'numVotes': [100, 150, 200]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt002'],
        'seasonNumber': [1, 1, 1, 2, 2],
        'episodeNumber': [0, 2, 0, 0, 2]
    })

    p = 1

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame({'numVotes': [100, 150], 'numberOfEpisodes': [2, 2]})

    assert msg == 'There were found 0 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_analysis3_some_series_removed():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004'],
        'averageRating': [7.5, 8.0, 9.0, 7.8],
        'numVotes': [100, 150, 200, 50]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005', 'ep006', 'ep007', 'ep008', 'ep009'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt002', 'tt003', 'tt003', 'tt004', 'tt004'],
        'seasonNumber': [1, 1, 1, 1, 2, 1, 2, 1, 1],
        'episodeNumber': [0, 1, 0, 1, 1, 2, 2, 3, 2]
    })

    p = 1

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame({
        'numVotes': [100, 150],
        'numberOfEpisodes': [1, 2],
    })

    assert msg == 'There were found 2 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_analysis3_some_series_removed_and_quantile_filter():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004'],
        'averageRating': [7.5, 8.0, 9.0, 7.8],
        'numVotes': [100, 150, 200, 50]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005', 'ep006', 'ep007', 'ep008', 'ep009', 'ep010'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt002', 'tt003', 'tt003', 'tt004', 'tt004', 'tt004'],
        'seasonNumber': [1, 1, 1, 1, 2, 1, 2, 1, 1, 1],
        'episodeNumber': [0, 1, 0, 1, 1, 2, 2, 0, 1, 2]
    })

    p = 0.5

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame({
        'numVotes': [100],
        'numberOfEpisodes': [1],
    })

    assert msg == 'There were found 1 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

def test_analysis3_no_series_remaining():
    ratings = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004'],
        'averageRating': [7.5, 8.0, 9.0, 7.8],
        'numVotes': [100, 150, 200, 50]
    })

    episodes = pd.DataFrame({
        'episodeId': ['ep001', 'ep002', 'ep003', 'ep004', 'ep005', 'ep006'],
        'tconst': ['tt001', 'tt001', 'tt002', 'tt002', 'tt003', 'tt004'],
        'seasonNumber': [1, 1, 1, 2, 1, 1],
        'episodeNumber': [2, 3, 2, 3, 3, 3]
    })

    p = 0.5

    result, msg = analysis3(ratings, episodes, p)

    expected_df = pd.DataFrame(columns=['numVotes', 'numberOfEpisodes'])

    assert msg == 'There were found 4 series with at least one season without first episode and were omitted during analysis 3.'
    assert_almost_equal(result.reset_index(drop=True), expected_df.reset_index(drop=True))

