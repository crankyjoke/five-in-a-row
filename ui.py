import tkinter as tk
from tkinter import messagebox
import sys
import os
from game_logic import FiveInARowMinMax
class FiveInARowGUI:
    def __init__(self, master, game_logic, multiplayer_mode=False):
        self.master = master
        self.master.title("Five in a Row")
        self.game_logic = game_logic
        self.multiplayer_mode = multiplayer_mode
        self.create_board_buttons()

        window_width = 100 * self.game_logic.board_size
        window_height = 100 * self.game_logic.board_size
        self.master.geometry(f"{window_width}x{window_height}")

    def create_board_buttons(self):
        self.buttons = [[None] * self.game_logic.board_size for _ in range(self.game_logic.board_size)]

        for i in range(self.game_logic.board_size):
            for j in range(self.game_logic.board_size):
                self.buttons[i][j] = tk.Button(
                    self.master,
                    text='',
                    width=6,
                    height=3,
                    padx=5,
                    pady=5,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.game_logic.make_move(row, col):
            self.buttons[row][col].config(text=self.game_logic.current_player)

            if self.game_logic.check_winner(row, col):
                self.show_winner()
            elif self.game_logic.is_board_full():
                self.show_draw()
            else:
                self.game_logic.switch_player()
                if not self.multiplayer_mode:
                    self.ai_turn()

    def ai_turn(self):
        if not self.game_logic.is_board_full() and not self.game_logic.check_winner(-1, -1):
            ai_move = self.game_logic.find_best_move()
            self.game_logic.make_move(*ai_move)
            self.buttons[ai_move[0]][ai_move[1]].config(text='O')

            if self.game_logic.check_winner(*ai_move):
                self.show_winner()
            elif self.game_logic.is_board_full():
                self.show_draw()
            else:
                self.game_logic.switch_player()

    def show_winner(self):
        winner = "Player X" if self.game_logic.current_player == 'X' else "Player O"
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_and_restart()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_and_restart()

    def reset_and_restart(self):
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")

        if play_again:
            self.master.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            self.master.destroy()
class ModeSelectionUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mode Selection")
        self.selected_mode = tk.StringVar(value="single_player")
        self.step_depth = tk.IntVar(value=1)

        label = tk.Label(self.master, text="Select Game Mode:")
        label.pack()

        single_player_button = tk.Radiobutton(
            self.master, text="Single Player (vs AI)", variable=self.selected_mode, value="single_player"
        )
        single_player_button.pack()

        two_players_button = tk.Radiobutton(
            self.master, text="Two Players (Human vs Human)", variable=self.selected_mode, value="two_players"
        )
        two_players_button.pack()

        depth_label = tk.Label(self.master, text="Select Step Depth (0-2):")
        depth_label.pack()

        depth_entry = tk.Entry(self.master, textvariable=self.step_depth)
        depth_entry.pack()

        start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        start_button.pack()

    def start_game(self):
        self.master.destroy()
        game_logic = FiveInARowMinMax(step_depth=self.step_depth.get())
        root = tk.Tk()

        if self.selected_mode.get() == "single_player":
            game = FiveInARowGUI(root, game_logic, multiplayer_mode=False)
        else:
            game = FiveInARowGUI(root, game_logic, multiplayer_mode=True)

        root.mainloop()