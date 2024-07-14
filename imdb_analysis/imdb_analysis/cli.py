import argparse
import matplotlib.pyplot as plt
from .preparations import prepare_frames
from .task1 import analysis1, analysis1_alternative
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
    parser.add_argument('-alternative', action='store_true', help='Use alternative version of analysis 1')
    
    args = parser.parse_args()
    try:
        basics = read_basics(args.basics, 'basics_cache.csv')
        ratings, akas, episodes = prepare_frames(read_frames(args), basics, args)
        
        if args.alternative:
            res1 = analysis1_alternative(akas, ratings, [(i + 1) * 10 for i in range
                                                         (20)], 10)
        else:
            res1 = analysis1(akas, ratings, [(i + 1) * 10 for i in range(20)], 10) 
        for lst in res1:
            print(lst)

        data = ratings.merge(akas, on = ['tconst'])
        statistics = ['gdp', 'gdp_pc', 'population']
        resources = read_resources(statistics)
        weak_hegemons = analysis2(data, resources, statistics, 'numVotes')
        strong_hegemons = analysis2(data, resources, statistics, 'quality')
        print('weak impact hegemons: ' + str(weak_hegemons)) 
        print('strong impact hegemons: ' + str(strong_hegemons)) 

        res3, msg = analysis3(ratings, episodes, 0.99)
        res3.plot.scatter(x='numVotes', y='numberOfEpisodes')
        plt.savefig('analysis3_plot.png')
        print(msg)

    except EmptySubsetChosen:
        print("No movies in given range.")

if __name__ == "__main__":
    main()
