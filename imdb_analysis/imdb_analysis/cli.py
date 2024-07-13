import argparse
import matplotlib.pyplot as plt
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
        basics = read_basics(args.basics, 'basics_cache.csv')
        ratings, akas, episodes = prepare_frames(read_frames(args), basics, args)
        data = ratings.merge(akas, on = ['tconst'])

        for lst in analysis1(data, [(i + 1) * 10 for i in range(20)], 10):
            print(lst)

        statistics = ['gdp', 'gdp_pc', 'population']
        resources = read_resources(statistics)
        weak_hegemons = analysis2(data, resources, statistics, 'numVotes')
        strong_hegemons = analysis2(data, resources, statistics, 'quality')
        print('weak impact hegemons: ' + str(weak_hegemons)) 
        print('strong impact hegemons: ' + str(strong_hegemons)) 

        res3, msg = analysis3(ratings, episodes, 0.99)
        res3.plot.scatter(x='numVotes', y='numberOfEpisodes')
        plt.show()
        print(msg)

    except EmptySubsetChosen:
        print("No movies in given range.")

if __name__ == "__main__":
    main()
