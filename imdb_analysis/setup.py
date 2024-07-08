from setuptools import setup, find_packages

setup(
    name='imdb_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scipy',
        'pandas',
        'matplotlib'],
    entry_points={
        'console_scripts': [
            'imdb_analysis=imdb_analysis.cli:main',
        ],
    },
    author='Krzysztof Hajderek',
    author_email='kh438485@students.mimuw.edu.pl',
    description='imdb analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.8',
)
