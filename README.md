
<h1> Tic-Tac-Toe-Python </h1>
This project demonstrates several topics including lambdas expressions, classes and object-oriented programming, exception handling, conditional statements, loops, and the use of external libraries (in this case, the `tabulate` library). 
<hr>

<h1>Project Structure</h1>

<b> <h3> Game Class </h3> It contains the actual Tic Tac Toe Game  without any additional features  </b>

Here is what each function does:
1. `__init__(self)`: Initializes the class object by creating a 3x3 grid to store the game state, and defining the win conditions for X and O.
2. `play_game(self)`: This function begins the game by drawing the board and returning the input from the user.
3. `draw_board(self)`: This function prints the current game board in a visually appealing way using the `tabulate` module.
4. `play_move(self, x, y, op)`: This function allows the player to make a move on the board. It updates the game board by placing the move on the given x and y coordinates, and then draws the updated board.
5. `input(self)`: This function takes input from the user and processes it. It splits the input string into two integers, checks if the input is within the valid range and if the chosen cell is unoccupied. If the input is valid, it makes a move by calling the `play_move` function, and then checks if the game has ended. If the game has ended, it returns a string indicating the winner or a draw.
6. `draw_condition(self)`: This function checks if the game is in a draw state. It checks if there are any empty cells left, if there is a winning row/column/diagonal, and if X and O both have equal number of moves.
7. `wins(self)`: This function checks if the game has ended and returns a value indicating the winner or a draw. It first checks if the game is in an impossible state, then checks for winning rows/columns/diagonals. If X wins, it returns 1; if O wins, it returns 0; otherwise, it returns -1.
8. `gameNotFinished(self)`: This function checks if the game has ended and returns True if it has not.
9. `is_unplayable(self)`: This function checks if the game is in an impossible state where both X and O have won, or if the difference between the number of moves made by X and O is greater than 1.
10. `diagonalMat(self)`: This function returns the two diagonals of the game board.
11. `colMat(self)`: This function returns the columns of the game board.
12. `countX(self)`: This function returns the number of moves made by X.
13. `countO(self)`: This function returns the number of moves made by O.
14. `has_empty_cells(self)`: This function checks if there are any empty cells left in the game board.  

<hr>

<b> <h3> Main Class </h3> It contains additional features of the tic tac toe game and is responsible for running the game</b>

Here is what each function does:
1. `__init__(self)`: This is the constructor method for the "Main" class. It initializes a "scanner" variable to an empty string and enters a while loop that runs until the user enters "3" to quit the game. Within the loop, it calls the "greet_user" method to display the game menu and prompts the user to enter a choice. Depending on the choice, it either calls the "play" method to start a new game, the "score_card" method to display the game statistics, or displays an error message for invalid input.
2. `play(self, n)`: This method takes an integer argument "n" that represents the number of games to be played. It then uses a for loop to play "n" games of Tic Tac Toe, keeping track of the score, number of draws, and printing the result of each game. It then calls the "add_score" method to update the game statistics.
3. `greet_user(self)`: This method simply displays a welcome message and the game menu using the "tabulate" module.
4. `add_score(self, n, score, c, draw)`:  This method takes four integer arguments "n", "score", "c", and "draw", representing the number of games played, the number of games won, the number of games lost, and the number of draws, respectively. It updates the global "parameters" variable, which is a tuple containing the total game statistics.
5. `score_card(self, total, x, y, draw)`: This method takes four integer arguments "total", "x", "y", and "draw", representing the total number of games played, the number of games won, the number of games lost, and the number of draws, respectively. It displays the game statistics in a table format using the "tabulate" module.
