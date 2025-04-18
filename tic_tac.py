import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title ("Tic Tac Toe")
        self.player = "X"
        self.comp = "0"
        self.board = [""] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial, 40"), width=5, height=2,
                               command=lambda i=i:self.player_move(i))


if __name__ == "__main__":
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()