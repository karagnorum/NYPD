import pandas as pd
from .exceptions import EmptySubsetChosen

def choose_years(df, fromYear, toYear, years):

    merged = df.merge(years, on=['tconst'])
    res = merged.loc[(merged['startYear'] >= fromYear) & (merged['startYear'] <= toYear)]
    res = res.drop('startYear', axis='columns')

    if res.empty: 
        raise EmptySubsetChosen

    return res

def prepare_frames(frames, basics, args):
    
    if args.start:
        if args.end:
            for i in range(len(frames)):
                frames[i] = choose_years(frames[i], args.start, args.end, basics)
        else:
            print("End of range not given, using whole dataset.")
    
    for frame in frames:
        frame.dropna(inplace=True)
    
    return frames

