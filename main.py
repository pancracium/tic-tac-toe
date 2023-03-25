"""Main file."""

###################################
# TIC-TAC-TOE [v0.3 (25-03-2023)] #
###################################

#Import necessary modules
import tkinter as tk
from app import TicTacToeApp

#Set up a window
WIDTH, HEIGHT = 1080, 720
root = tk.Tk()
app = TicTacToeApp(master=root)
app.master.mainloop()