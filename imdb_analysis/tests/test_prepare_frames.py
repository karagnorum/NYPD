import pytest
import pandas as pd
from argparse import Namespace
from imdb_analysis.preparations import prepare_frames 

def test_prepare_frames_filters_by_years():
    # Prepare sample data
    frames = [
        pd.DataFrame({
            'tconst': ['tt001', 'tt002', 'tt003'],
            'value': [1.0, 2.0, 3.0]
        }),
        pd.DataFrame({
            'tconst': ['tt001', 'tt004', 'tt005'],
            'value': [1.0, 2.0, 3.0]
        })
    ]
    years = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004', 'tt005'],
        'startYear': [1999, 2000, 2001, 2002, 2003]
    })
    args = Namespace(start=2000, end=2002)

    # Call the function
    result = prepare_frames(frames, years, args)

    # Expected result
    expected = [
        pd.DataFrame({
            'tconst': ['tt002', 'tt003'],
            'value': [2.0, 3.0]
        }),
        pd.DataFrame({
            'tconst': ['tt004'],
            'value': [2.0]
        })
    ]

    # Check the result
    for res, exp in zip(result, expected):
        pd.testing.assert_frame_equal(res.reset_index(drop=True), exp.reset_index(drop=True))

def test_prepare_frames_removes_missing_and_filters_years():
    # Prepare sample data
    frames = [
        pd.DataFrame({
            'tconst': ['tt001', 'tt002', 'tt003'],
            'value': [1, float('nan'), 3.0]
        }),
        pd.DataFrame({
            'tconst': ['tt001', 'tt004', 'tt005'],
            'value': [float('nan'), 2.0, 3.0]
        })
    ]
    years = pd.DataFrame({
        'tconst': ['tt001', 'tt002', 'tt003', 'tt004', 'tt005'],
        'startYear': [1999, 2000, 2001, 2002, 2003]
    })
    args = Namespace(start=1999, end=2002)

    # Call the function
    result = prepare_frames(frames, years, args)

    # Expected result
    expected = [
        pd.DataFrame({
            'tconst': ['tt001', 'tt003'],
            'value': [1.0, 3.0]
        }),
        pd.DataFrame({
            'tconst': ['tt004'],
            'value': [2.0]
        })
    ]

    # Check the result
    for res, exp in zip(result, expected):
        pd.testing.assert_frame_equal(res.reset_index(drop=True), exp.reset_index(drop=True))

test_prepare_frames_removes_missing_and_filters_years()
test_prepare_frames_filters_by_years()