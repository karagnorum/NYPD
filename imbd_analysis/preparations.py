import pandas as pd
from read import *
from exceptions import EmptySubsetChosen

def choose_years(df, fromYear, toYear, years):

    df.reset_index(inplace=True)
    merged = df.merge(years, on=['tconst'])
    res = merged.loc[(merged['startYear'] >= fromYear) & (merged['startYear'] <= toYear)]
    res = res.drop('startYear', axis='columns')

    if res.empty: 
        raise EmptySubsetChosen

    return res

def get_frames(args):
    
    frames = read_frames(args)

    if args.start:
        if args.end:
            basics = read_basics(args.basics, 'basics_cache.csv')
            print(basics.columns)
            try:
                for i in range(len(frames)):
                    frames[i] = choose_years(frames[i], args.start, args.end, basics)
            except EmptySubsetChosen:
                print("No movies in given range.")
                return
        else:
            print("End of range not given, using whole dataset.")
    
    for frame in frames:
        frame.dropna(inplace=True)
    
    return frames

