import argparse
import matplotlib.pyplot as plt
from .preparations import prepare_frames
from .task1 import analysis1, analysis1_alternative
from .task2 import analysis2
from .task3 import analysis3
from .read import *
from .exceptions import EmptySubsetChosen

def run_analysis(args):
    try:
        years = read_years(args.basics)
        ratings, regions, episodes = prepare_frames(read_frames(args), years, args)
        
        # task 1
        # We want ranks for 10, 20, ..., 200 best movies
        rank_lengths = [(i + 1) * 10 for i in range (20)]
        if args.alternative:
            #if specified, use alternative version of analysis 1
            res1 = analysis1_alternative(regions, ratings, rank_lengths, 10)
        else:
            res1 = analysis1(regions, ratings, rank_lengths, 10) 
        # print 10 top countries for every case
        for lst in res1:
            print(lst)
            
        #task 2
        data = ratings.merge(regions, on = ['tconst'])
        #statistics used in analysis 2, gdp_pc = GDP per capita
        statistics = ['gdp', 'gdp_pc', 'population']
        resources = read_resources(statistics)
        #hegemons with respect to weak impact
        weak_hegemons = analysis2(data, resources, statistics, 'numVotes')
        #hegemons with respect to strong impact
        strong_hegemons = analysis2(data, resources, statistics, 'quality')
        print('weak impact hegemons: ' + str(weak_hegemons)) 
        print('strong impact hegemons: ' + str(strong_hegemons)) 

        #task 3
        res3, msg = analysis3(ratings, episodes, 0.99)
        #plot result od analysis 3
        res3.plot.scatter(x='numVotes', y='numberOfEpisodes')
        plt.show()
        # print message about ommited series
        print(msg)

    except EmptySubsetChosen:
        print("No movies in given range.")

def main():
    parser = argparse.ArgumentParser(description="Imdb movies analysis")
    parser.add_argument('ratings', type=str, help='Path to ratings.tsv')
    parser.add_argument('akas', type=str, help='Path to akas.tsv')
    parser.add_argument('basics', type=str, help='Path to title.basics.tsv')
    parser.add_argument('episodes', type=str, help='Path to title.episode.tsv')
    parser.add_argument('-start', type=int, help='Start year for analysis', 
                        required=False)
    parser.add_argument('-end', type=int, help='End year for analysis', required=False)
    parser.add_argument('-alternative', action='store_true', help="""Use alternative 
                        version of analysis 1""")
    
    args = parser.parse_args()
    run_analysis(args)

if __name__ == "__main__":
    main()
