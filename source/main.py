import argparse
from read import *
from lib import choose_years
from task1 import analysis1
from task2 import analysis2
from exceptions import EmptySubsetChosen

def main():
    
    parser = argparse.ArgumentParser(description="Imdb movies analysis")
    parser.add_argument('ratings', type=str, help='Path to ratings.tsv')
    parser.add_argument('akas', type=str, help='Path to akas.tsv')
    parser.add_argument('basics', type=str, help='Path to title.basics.tsv')
    parser.add_argument('episodes', type=str, help='Path to title.episode.tsv')
    parser.add_argument('-start', type=int, help='Start year for analysis', required=False)
    parser.add_argument('-end', type=int, help='End year for analysis', required=False)
    
    args = parser.parse_args()
    frames = get_frames(args)
    ratings, akas, episodes = frames

    if args.start:
        if args.end:
            basics = read_basics(akas, args.basics, 'basics_cache.csv')
            frames.append(basics)
            try:
                for i in [0, 1]:
                    frames[i] = choose_years(frames[i], args.start, args.end, basics[['tconst', 'startYear']])
            except EmptySubsetChosen:
                print("No movies in given range.")
                return
        else:
            print("End of range not given, using whole dataset.")
    
    for frame in frames:
        frame.dropna()

    # analysis1(akas, ratings)
    analysis2(akas, ratings)
    
    

if __name__ == "__main__":
    main()
