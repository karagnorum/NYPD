import argparse
from read import read_frames
from lib import choose_years
from task1 import analysis1
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
    frames = read_frames(args)
    basics = frames[2]

    if args.start:
        if args.end:
            try:
                for i in [0, 1]:
                    frames[i] = choose_years(frames[i], args.start, args.end, basics[['tconst', 'startYear']])
            except EmptySubsetChosen:
                print("No movies in given range.")
                return
        else:
            print("End of range not given, using whole dataset.")
    
    ratings, akas, basics, episodes = frames

    analysis1(akas, ratings)
            
    
    

if __name__ == "__main__":
    main()
