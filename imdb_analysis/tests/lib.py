import pandas as pd

def assert_almost_equal(result, expected):
    """Test for equality of data frames, disregarding order of rows and dtypes."""
    pd.testing.assert_frame_equal(result.sort_values(by=result.columns[0]).reset_index(drop=True), expected.sort_values(by=expected.columns[0]).reset_index(drop=True), check_dtype=False)