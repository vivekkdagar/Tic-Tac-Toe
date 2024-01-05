from game import Game
from tabulate import tabulate

parameters = None
    
class Main:
    def __init__(self):
        scanner = ""
        
        while scanner != "3":
            self.greet_user()
            scanner = input("Enter your choice: ")

            if scanner == "1":
                self.play(int(input("Enter number of matches: ")))
            elif scanner == "2":
                if parameters == None:
                    print("Haven't played any matches yet!")
                else:
                    self.score_card(*parameters)
            elif scanner == "3":
                print("Thanks for playing!")
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
    
    def play(self, n: int) -> None:
        global parameters
        score = draw = 0
        for i in range(n):
            temp = Game().play_game()
            print(temp)
            if temp == "X wins":
                score += 1
            if temp == "Draw":
                draw += 1
        self.add_score(n, score, n-score-draw, draw)
        
    def greet_user(self) -> None:
        print(tabulate([], headers = ["Welcome to Tic Tac Toe"], tablefmt="grid", showindex = False))
        table = [["1.", "Play"], ["2.", "Scores"], ["3.", "Quit"]]
        print(tabulate(table, headers = ["Select an option"], tablefmt="grid"))
    
    def add_score(self, n: int, score: int, c: int, draw: int) -> None:
        global parameters
        if parameters == None:
            parameters = (n, score, c, draw)
        else:
            parameters = tuple(map(sum, zip(parameters, (n, score, c, draw))))
        return parameters
            
    def score_card(self, total: int, x: int, y: int, draw: int) -> None:
        headers = ["Total", "You Won", "You Lost", "Draw"]
        grid = [[total, x, y, draw]]
        print(tabulate(grid, headers, tablefmt="grid"))
