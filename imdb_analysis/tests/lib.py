import pandas as pd

def assert_almost_equal(result, expected):
    pd.testing.assert_frame_equal(result.sort_values(by=result.columns[1]).reset_index(drop=True), expected)