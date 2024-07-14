import os
from imdb_analysis.cli import run_analysis
from argparse import Namespace

def test_run_analysis(capsys):
    test_dir = os.path.dirname(__file__)
    args = ['ratings_test.tsv', 'akas_test.tsv', 'title.basics_test.tsv', 'title.episode_test.tsv']
    for i in range(len(args)):
        args[i] = os.path.join(test_dir, 'data', args[i])
    args = Namespace(ratings=args[0], akas=args[1], basics=args[2], episodes=args[3], start=1500, end=2500, alternative=False)
    
    run_analysis(args)

    # Capture the output
    captured = capsys.readouterr()
    expected_output_path = os.path.join(test_dir, 'data', 'output.txt')
    with open(expected_output_path, 'r') as f:
        assert captured.out == f.read()
    