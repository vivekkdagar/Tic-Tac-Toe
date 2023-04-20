## Documentation

### Introduction

The "Tic Tac Toe" game is a two-player game played on a 3x3 grid. Each player takes turns placing their mark ('X' or 'O') on the grid until one player gets three marks in a row (horizontally, vertically or diagonally) or the game ends in a draw. This project demonstrates several topics including lambdas expressions, classes and object-oriented programming, exception handling, conditional statements, loops, and the use of external libraries (in this case, the `tabulate` library). 

### Installation

This game requires the `tabulate` module, which can be installed using pip:
```
pip install tabulate
```

### Usage

To start the game, run the `Main()` constructor from the `main.py` file:
```python
from main import Main

Main()
```

The game has a menu with the following options:
1. Play game
2. View score card
3. Quit

#### Play game

Choose option 1 to play the game. Enter the number of matches you want to play and start playing. After each match, the result will be displayed on the screen.

#### View score card

Choose option 2 to view the score card. The score card will display the number of matches played, the number of matches won by player X, the number of matches won by player O, and the number of draws.

#### Quit

Choose option 3 to quit the game.

### Classes

#### Game

This class represents the Tic Tac Toe game. It has the following methods:
* `__init__`: Initializes the game board and the win conditions for player X and player O.
* `play_game`: Draws the board and takes the input from the user.
* `draw_board`: Draws the current state of the board in a visually appealing way using the `tabulate` module.
* `play_move`: Places the mark of the current player on the board. It updates the game board by placing the move on the given x and y coordinates, and then draws the updated board.
* `input`: Takes the input from the user and validates it. It splits the input string into two integers, checks if the input is within the valid range and if the chosen cell is unoccupied. If the input is valid, it makes a move by calling the `play_move` function, and then checks if the game has ended. If the game has ended, it returns a string indicating the winner or a draw.
* `draw_condition`: Checks if the game has ended in a draw.
* `wins`: Checks if the game has ended and returns the winner. If X wins, it returns 1; if O wins, it returns 0; otherwise, it returns -1.
* `gameNotFinished`: Checks if the game is not finished yet.
* `is_unplayable`: Checks if the game is in an impossible state where both X and O have won, or if the difference between the number of moves made by X and O is greater than 1.
* `diagonalMat`: Returns the two diagonals of the board.
* `colMat`: Returns the columns of the board.
* `countX`: Counts the number of 'X' marks on the board.
* `countO`: Counts the number of 'O' marks on the board.
* `has_empty_cells`: Checks if the board has any empty cells.

#### Main

This class represents the main menu of the game and is responsible for running the game. It has the following methods:
* `__init__`: This is the constructor method for the "Main" class. It initializes a "scanner" variable to an empty string and enters a while loop that runs until the user enters "3" to quit the game. Within the loop, it calls the "greet_user" method to display the game menu and prompts the user to enter a choice. Depending on the choice, it either calls the "play" method to start a new game, the "score_card" method to display the game statistics, or displays an error message for invalid input.
* `play`: This method takes an integer argument "n" that represents the number of games to be played. It then uses a for loop to play "n" games of Tic Tac Toe, keeping track of the score, number of draws, and printing the result of each game. It then calls the "add_score" method to update the game statistics.
* `score_card`: This method takes four integer arguments "total", "x", "y", and "draw", representing the total number of games played, the number of games won, the number of games lost, and the number of draws, respectively. It displays the game statistics in a table format using the "tabulate" module.
* `greet_user`: This method simply displays a welcome message and the game menu using the "tabulate" module.
* `add_score`: This method takes four integer arguments "n", "score", "c", and "draw", representing the number of games played, the number of games won, the number of games lost, and the number of draws, respectively. It updates the global "parameters" variable, which is a tuple containing the total game statistics.

