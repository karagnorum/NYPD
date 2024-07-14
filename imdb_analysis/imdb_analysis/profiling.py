import cProfile
import pstats
import imdb_analysis.cli

def main():
    imdb_analysis.cli.main()

if __name__ == '__main__':
    profiler = cProfile.Profile()
    
    # Run the main function with profiling
    profiler.run('main()')
    
    # Create a file to save profiling results
    with open('profiling_results.prof', 'w') as f:
        ps = pstats.Stats(profiler, stream=f)
        ps.strip_dirs().sort_stats('cumulative')
        ps.print_stats()
