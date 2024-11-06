from ui import ModeSelectionUI
import tkinter as tk
from tkinter import messagebox
import sys
import os




if __name__ == "__main__":
    mode_selection_root = tk.Tk()
    mode_selection_ui = ModeSelectionUI(mode_selection_root)
    mode_selection_root.mainloop()
