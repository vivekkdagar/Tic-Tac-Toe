#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from game import Game
from prettytable import PrettyTable
from tabulate import tabulate

class Interface:
    def __init__(self):
        try:
            self.x = Game()
            self.x.symbols()
            self.start()
        except KeyboardInterrupt:
            print('Bye')
            exit()
    
    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                self.x.play_game('h')
            elif choice == "2":
                self.x.play_game('c')
            elif choice == "3":
                self.x.score_card.display_statistics()
            elif choice == "4":
                print('Bye')
                exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def display_menu(self):
        menu = PrettyTable()
        menu.field_names = ["Choice", "Option"]
        
        menu.add_row(["1.", "Play against human"])
        menu.add_row(["2.", "Play against computer"])
        menu.add_row(["3.", "Check scores"])
        menu.add_row(["4.", "Quit"])
        
        print(tabulate(menu, headers=["Select an option"], tablefmt="grid"))

if __name__ == "__main__":
    Interface()