import pandas as pd
from exceptions import EmptySubsetChosen

def choose_years(df, fromYear, toYear, years):

    merged = df.merge(years, on=['tconst'])
    res = merged.loc[(merged['startYear'] >= fromYear) & (merged['startYear'] <= toYear)]

    if res.empty: 
        raise EmptySubsetChosen

    return res

