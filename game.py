from tabulate import tabulate

class Game:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.win_condition_x = ['X', 'X', 'X']
        self.win_condition_o = ['O', 'O', 'O']

    def play_game(self):
        self.draw_board()
        return self.input()

    def draw_board(self):
        print(tabulate(self.grid, tablefmt="fancy_grid"))

    def play_move(self, x, y, op):
        self.grid[x - 1][y - 1] = op
        self.draw_board()
    
    def input(self):
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
                self.play_move(xCor, yCor, 'X' if moves % 2 else 'O')
                moves += 1
                if self.wins() == 1:
                    return "X wins"
                elif self.wins() == 0:
                    return "O wins"
                elif self.draw_condition():
                    return "Draw"
            except:
                print("Please enter numbers only!")
    
    def draw_condition(self):
        if (self.is_unplayable() or self.has_empty_cells() or (abs(self.countO() - self.countX()) >= 2) or (self.countX() + self.countO() != 9)): # It isn't a draw if it has empty cells
            return False
    
        for i in range(3): # Rows checked
            if (self.grid[i] == self.win_condition_x or self.grid[i] == self.win_condition_o):
                return False
    
        diagonal = self.diagonalMat()
        for chars in diagonal: # Diagonal checked
            if (chars == self.win_condition_x or chars == self.win_condition_o):
                return False
    
        colMat = self.colMat()
        for chars in colMat:
            if (chars == self.win_condition_x or chars == self.win_condition_o):
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
