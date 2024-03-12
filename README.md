<a href='https://github.com/vivekkdagar/Boggle-Word-Solver/blob/main/LICENSE' target="_blank"><img alt='GitHub' src='https://img.shields.io/badge/GNU_General Public License-100000?style=for-the-badge&logo=GitHub&logoColor=white&labelColor=black&color=black'/></a>

### Updates to the Tic Tac Toe Project
> #### 3. Improved GUI
> We understand the importance of a visually appealing and intuitive user interface. The project will be updated to include an improved graphical user interface (GUI) for a more engaging and enjoyable gaming experience.
> #### 4. Package Distribution - .deb and .exe
> To simplify the installation process, we will be providing Debian (.deb) packages for Linux systems and executable (.exe) files for Windows. This will make it easier for users to install and run the Tic Tac Toe game without worrying about dependencies or setup complexities.
> #### 5. Working on a peer to peer connection as well: Youo'll be able to play locally on lan
> Stay tuned for these exciting updates, and enjoy an even better Tic Tac Toe gaming experience! If you have any suggestions or feedback, feel free to let us know.

# Tic Tac Toe
> A Python Tic Tac Toe game played by two-players on a 3x3 grid. (Due to this project being updated, this documentation will be updated as well). <br><br>
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Play game](#play-game)
   - [View score card](#view-score-card)
   - [Quit](#quit)
4. [Working](#working)
   - [Game](#game)
   - [Main](#main)
5. [Conclusion](#conclusion)

## 1. Introduction<a name="introduction"></a>

Tic Tac Toe is a classic two-player game played on a 3x3 grid. The objective is to get three marks ('X' or 'O') in a row (horizontally, vertically, or diagonally) or end the game in a draw. This project showcases various programming concepts, including lambda expressions, classes, object-oriented programming, exception handling, conditional statements, loops, and the use of the `tabulate` library.

## 2. Installation<a name="installation"></a>

To run this game, you need the `tabulate` module, which you can install using pip or conda:

```bash
pip install tabulate
# OR
conda install tabulate
```

## 3. Usage<a name="usage"></a>

To play the game, execute the `Main()` constructor from the `main.py` file:

```python
from main import Main

Main()
```

The game features a menu with the following options:

### Play game<a name="play-game"></a>

Select option 1 to start a game. Enter the number of matches you want to play and begin playing. After each match, the result will be displayed on the screen.

### View score card<a name="view-score-card"></a>

Choose option 2 to view the score card. The score card displays the number of matches played, matches won by player X, matches won by player O, and the number of draws.

### Quit<a name="quit"></a>

Select option 3 to exit the game.

## 4. Working<a name="working"></a>

### Game<a name="game"></a>

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

### Main<a name="main"></a>

The `Main` class represents the game's main menu and handles game execution. It provides the following methods:

- `__init__`: Constructor for the `Main` class, displaying the menu and processing user choices.
- `play`: Starts and manages Tic Tac Toe games based on the specified count.
- `score_card`: Displays game statistics, including total games played, games won, games lost, and draws, in a tabulated format.
- `greet_user`: Shows a welcome message and the game menu.
- `add_score`: Updates the global game statistics.

## 5. Conclusion<a name="conclusion"></a>

This documentation has provided insights into the Tic Tac Toe project, covering its purpose, installation, usage, and internal workings. Whether you're a player or a developer interested in the code, enjoy playing Tic Tac Toe! If you have any questions or need further assistance, feel free to ask.
