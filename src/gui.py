#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class TicTacToe:
    def __init__(self):
       self.root = ctk.CTk()  # Use CTk() for the main window
       self.root.title("Tic Tac Toe")

       # Create a 3x3 grid of buttons using CTkButton
       self.buttons = [[None, None, None] for _ in range(3)]
       for i in range(3):
           for j in range(3):
               self.buttons[i][j] = ctk.CTkButton(self.root, text="", text_font=("Helvetica", 16), width=8, height=4, command=lambda row=i, col=j: self.on_button_click(row, col))
               self.buttons[i][j].grid(row=i, column=j)

       # Variable to track current player (X or O)
       self.current_player = 'X'

    def on_button_click(self, row, col):
        # Check if the button is already clicked or if the game is over
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                # Switch player
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True  # Check row
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True  # Check column
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True  # Check diagonal
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True  # Check diagonal
        return False

    def check_tie(self):
        # Check if all buttons are clicked (tie)
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False  # Game not tied
        return True  # Game is tied

    def reset_game(self):
        # Reset the game by clearing all button texts
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
