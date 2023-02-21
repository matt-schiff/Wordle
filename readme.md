# Project Title

A set of command line scripts that allow users to play wordle, solve wordles, and play octordles.

## Description

1. Wordle.py: play a game of wordle
2. WordleHelper.py: provides a suggested set of guesses for a wordle
3. WordleSolver.py: backbone for WordleHelper, creates and prunes a list of words to create guesses
4. WordSelector.py: alternative models for selecting guesses
5. antiwordle.py: the opposite of wordle, the goal is to last as long as possible playing with hard mode rules without guessing the word.
6. octordle.py: Like wordle, but you are attempting to solve 8 wordles simultaneously.
7. .txt files: list of all valid guesses and valid words that can be guessed.

## Getting Started

### Dependencies

* Python 3

### Installing

* Clone the repo to your local machine

### Executing program

* All scripts can be found in the Scripts folder
* Run the python script for the game/program you want to run

```
python3 Wordle.py
```

## Authors

Contributors names and contact info

Matthew Schiff
mschiff@alumni.ncsu.edu

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [Official Wordle game](https://www.nytimes.com/games/wordle/index.html)
* [Official Octordle game](https://octordle.com)
