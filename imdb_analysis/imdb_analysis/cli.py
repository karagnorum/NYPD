import argparse
from .preparations import prepare_frames
from .task1 import analysis1
from .task2 import analysis2
from .task3 import analysis3
from .read import *
from .exceptions import EmptySubsetChosen

def main():
    
    parser = argparse.ArgumentParser(description="Imdb movies analysis")
    parser.add_argument('ratings', type=str, help='Path to ratings.tsv')
    parser.add_argument('akas', type=str, help='Path to akas.tsv')
    parser.add_argument('basics', type=str, help='Path to title.basics.tsv')
    parser.add_argument('episodes', type=str, help='Path to title.episode.tsv')
    parser.add_argument('-start', type=int, help='Start year for analysis', required=False)
    parser.add_argument('-end', type=int, help='End year for analysis', required=False)
    
    args = parser.parse_args()
    try:
        ratings, akas, episodes = prepare_frames(read_frames(args), read_basics(args.basics, 'basics_cache.csv'), args)
    except EmptySubsetChosen:
        print("No movies in given range.")
        return

    data = analysis1(akas, ratings)
    analysis2(data)
    analysis3(ratings, episodes)
    
    

if __name__ == "__main__":
    main()
