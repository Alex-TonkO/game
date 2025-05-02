import tkinter as tk
import random
from config_snake import *


class SnakeGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.resizable(False, False)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG)
        self.canvas.pack()
        self.menu_frame = tk.Frame(root)
        self.level = tk.StringVar(value="Medium")
        self.score = 0
        self.running = False
        self.paused = False
        self.after_id = None
        self.create_menu()

    def create_menu(self):
        self.clear_canvas()
        tk.Label(self.menu_frame, text="Menu", font=("Arial", 16)).pack()
        tk.Button(self.menu_frame, text="Start", font=("Arial", 16), command=self.start_game).pack()
        tk.OptionMenu(self.menu_frame, self.level, *SPEEDS.keys()).pack()
        tk.Button(self.menu_frame, text="Exit", font=("Arial", 16), command=root.destroy).pack()
        self.menu_frame.pack()

    def start_game(self):
        self.menu_frame.pack_forget()

    def clear_canvas(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    snake = SnakeGame(root)
    root.mainloop()
