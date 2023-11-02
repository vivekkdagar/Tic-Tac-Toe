# Tic Tac Toe

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

## Introduction

Tic Tac Toe is a classic two-player game played on a 3x3 grid. The objective is to get three marks ('X' or 'O') in a row (horizontally, vertically, or diagonally) or end the game in a draw. This project showcases various programming concepts, including lambda expressions, classes, object-oriented programming, exception handling, conditional statements, loops, and the use of the `tabulate` library.

## Installation

To run this game, you need the `tabulate` module, which you can install using pip or conda:

```bash
pip install tabulate
# OR
conda install tabulate
```

## Usage

To play the game, execute the `Main()` constructor from the `main.py` file:

```python
from main import Main

Main()
```


The game features a menu with the following options:

1. Play game
2. View score card
3. Quit

### Play game

Select option 1 to start a game. Enter the number of matches you want to play and begin playing. After each match, the result will be displayed on the screen.

### View score card

Choose option 2 to view the score card. The score card displays the number of matches played, matches won by player X, matches won by player O, and the number of draws.

### Quit

Select option 3 to exit the game.

## Working

### Game

The `Game` class represents the Tic Tac Toe game. It provides the following methods:

- `__init__`: Initializes the game board and win conditions for player X and player O.
- `play_game`: Draws the board and takes input from the user.
- `draw_board`: Displays the current board state using the `tabulate` module.
- `play_move`: Places the current player's mark on the board, updates the game board, and draws the updated board.
- `input`: Takes and validates user input, checks for valid range and unoccupied cells, and handles moves.
- `draw_condition`: Checks for a draw in the game.
- `wins`: Determines the winner (1 for X, 0 for O, -1 for no winner yet).
- `gameNotFinished`: Checks if the game is still in progress.
- `is_unplayable`: Identifies impossible game states, e.g., both X and O winning.
- `diagonalMat`: Returns the two diagonals of the board.
- `colMat`: Returns the columns of the board.
- `countX`: Counts the number of 'X' marks.
- `countO`: Counts the number of 'O' marks.
- `has_empty_cells`: Checks for empty cells on the board.

### Main

The `Main` class represents the game's main menu and handles game execution. It provides the following methods:

- `__init__`: Constructor for the `Main` class, displaying the menu and processing user choices.
- `play`: Starts and manages Tic Tac Toe games based on the specified count.
- `score_card`: Displays game statistics, including total games played, games won, games lost, and draws, in a tabulated format.
- `greet_user`: Shows a welcome message and the game menu.
- `add_score`: Updates the global game statistics.
