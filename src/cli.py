from prettytable import PrettyTable
from statistics import Statistics
from tabulate import tabulate

def handle_abort():
    print("\nGame aborted. Thanks for playing!")
    exit()

class Game:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.win_condition_x = ['X', 'X', 'X']
        self.win_condition_o = ['O', 'O', 'O']

    def play_game(self, player1, player2):
        try:
            self.draw_board()
            result = self.input(player1, player2)
            # Update statistics based on the game result
            if result == "X wins" and player1 == "X":
                result = "Player 1 wins"
            elif result == "O wins" and player1 == "O":
                result = "Player 1 wins"
            Statistics().update_statistics(result, True)
            if result == "Player 1 wins":
                Statistics().update_statistics("Player 1 wins against Human", False)
            if result not in ["Draw", "Player 1 wins"]:
                result = "Player 1 Lost"
            return result
        except KeyboardInterrupt:
            handle_abort()

    def draw_board(self):
        print(tabulate(self.grid, tablefmt="fancy_grid"))

    def play_move(self, x, y, op):
        self.grid[x - 1][y - 1] = op
        self.draw_board()
    
    def input(self, player1: str, player2: str):
        moves = 1
        flag = False
        while not flag:
            try:
                # Split the input by space and convert to integers
                xCor, yCor = map(int, input().split())
                if xCor > 3 or yCor > 3:
                    print("Coordinates should be from 1 to 3!")
                    continue
                if self.grid[xCor - 1][yCor - 1] != ' ':
                    print("This cell is occupied! Choose another one!")
                    continue
                self.play_move(xCor, yCor, player1 if moves % 2 else player2)
                moves += 1
                if self.wins() == 1:
                    return "X wins"
                elif self.wins() == 0:
                    return "O wins"
                elif self.draw_condition():
                    return "Draw"
            except KeyboardInterrupt:
                handle_abort()
            except:
                print("Please enter numbers only!")
    
    def draw_condition(self):
        if self.is_unplayable() or self.has_empty_cells() or (abs(self.countO() - self.countX()) >= 2) or (self.countX() + self.countO() != 9):
            return False
    
        # Rows, diagonals, and columns checked
        for line in self.grid + self.diagonalMat() + self.colMat():
            if line in [self.win_condition_x, self.win_condition_o]:
                return False

        return True

    
    def wins(self):
        if self.is_unplayable():
            return -1
        # Check all rows
        for row in self.grid + self.colMat() + self.diagonalMat():
            # If X wins return 1
            if row == self.win_condition_x:
                return 1
            # If O wins return 0
            elif row == self.win_condition_o:   # Else O won, then return 0
                return 0
        return -1
    
    def gameNotFinished(self):
        if not self.hasEmptyCells() or self.isUnplayable():
            return False
        return not any(row in [self.win_condition_x, self.win_condition_o] for row in self.grid + self.colMat() + self.diagonalMat())

    def is_unplayable(self): # is in an impossible state
        if (abs(self.countO() - self.countX()) >= 2) and (self.countX() + self.countO() != 9):
            return True
        xWins = sum(row == self.win_condition_x for row in self.grid + self.colMat() + self.diagonalMat())
        oWins = sum(row == self.win_condition_o for row in self.grid + self.colMat() + self.diagonalMat())
        return xWins >= 1 and oWins >= 1

    def diagonalMat(self):
        return [[self.grid[i][i] for i in range(3)], [self.grid[i][2-i] for i in range(3)]]

    def colMat(self):
        return [[self.grid[i][j] for i in range(3)] for j in range(3)]

    def countX(self):
        return sum(self.grid[i][j] == 'X' for i in range(3) for j in range(3))
    
    def countO(self):
        return sum(self.grid[i][j] == 'O' for i in range(3) for j in range(3))
    
    def has_empty_cells(self):
        return any("_" in chars or " " in chars for chars in self.grid)


class TicTacToe:
    def __init__(self):
        try:
            self.play()
        except KeyboardInterrupt:
            self.handle_abort()

    def play(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                self.play_game()
            elif choice == "2":
                print("Play against Computer (Coming Soon)")
            elif choice == "3":
                self.handle_abort()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def play_game(self):
        try:
            symbol_player1 = input("Enter your symbol, Player 1 (X/O): ").upper()
            while symbol_player1 not in ['X', 'O']:
                print("Invalid choice. Please enter 'X' or 'O'.")
                symbol_player1 = input("Enter your symbol, Player 1 (X/O): ").upper()
            symbol_player2 = "X" if symbol_player1 == "O" else "O"
            self.play_single_game(symbol_player1, symbol_player2)

            while True:
                try_again = self.display_try_again_menu()
                if try_again == "1":
                    self.play_single_game(symbol_player1, symbol_player2)
                elif try_again == "2":
                    print("Play against Computer (Coming Soon)")
                elif try_again == "3":
                    handle_abort()
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            self.handle_abort()

    def play_single_game(self, symbol_player1, symbol_player2):
        result = Game().play_game(symbol_player1, symbol_player2)
        print(result)
        Statistics().display_statistics()

    def handle_abort(self):
        print("\nGame aborted. Thanks for playing!")
        exit()

    def display_menu(self):
        print(tabulate([], headers=["Welcome to Tic Tac Toe"], tablefmt="grid", showindex=False))
        menu_options = [
            ["1.", "Play against another player"],
            ["2.", "Play against Computer (Coming Soon)"],
            ["3.", "Quit"]
        ]
        print(tabulate(menu_options, headers=["Select an option"], tablefmt="grid"))

    def display_try_again_menu(self):
        try_again_table = PrettyTable()
        try_again_table.field_names = ["Choice", "Option"]
        try_again_table.add_row(["1.", "Try again"])
        try_again_table.add_row(["2.", "Play against Computer (Coming Soon)"])
        try_again_table.add_row(["3.", "Quit"])

        print("\n")
        print(try_again_table)

        return input("Enter your choice (1/2/3): ")

if __name__ == "__main__":
    TicTacToe()
