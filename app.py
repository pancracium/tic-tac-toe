"""Create a new file for better organization."""

#Import necessary modules
import tkinter as tk
import randommove

class TicTacToeApp:
    """Create a class for the app."""
    def __init__(self, master=tk.Tk, width:int=1080, height:int=720):
        #Set up the window's title, size, position and icon
        global WIDTH, HEIGHT
        WIDTH, HEIGHT = width, height
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.geometry(f"{WIDTH}x{HEIGHT}+{self.master.winfo_screenwidth() // 2 - WIDTH // 2}+{self.master.winfo_screenheight() // 2 - HEIGHT // 2}")
        self.master.iconbitmap("icon.ico")
        #Set up some other attributes
        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.font = ("Consolas", 100, "bold")
        self.random_button_font = ("Consolas", 20, "bold")
        #Create the widgets
        self.create_widgets()

    def create_widgets(self):
        """Create some buttons where the X's and O's are placed."""
        #Create the buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text="", font=self.font, width=2, height=1,
                                   background="grey75", relief="flat", activebackground="grey75",
                                   borderwidth=0, highlightthickness=0,
                                   command=lambda x=i, y=j: self.play(x, y))
                button.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
                row.append(button)
            self.buttons.append(row)
        #Center the buttons
        for i in range(3):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1)
        #Button for playing a random move
        self.random_button = tk.Button(self.master, text="Random Move", font=self.random_button_font, width=5, height=1,
                               background="grey75", relief="flat", activebackground="grey75",
                               borderwidth=0, highlightthickness=0,
                               command=lambda: randommove.play(self))
        self.random_button.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    def play(self, x, y) -> str:
        """Make the game work."""
        #Only allow clicks on buttons that are not green
        if self.buttons[x][y]["background"] == "green":
            return "GreenButtonPressed"
        #Put X's and O's in the buttons
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            self.buttons[x][y].config(text=self.current_player)
            #Check if there's a winner
            if self.check_win():
                self.master.after(1000, lambda: self.master.title(f"{self.current_player} wins!"))
            elif self.check_tie():
                self.master.title("It's a tie")
                self.master.after(1000, lambda: self.reset())
            else:
                #Change turns
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"
        self.master.title(f"{self.current_player}'s turn")

    def check_win(self) -> bool:
        """Check if there's a winner and show where the player won."""
        #Check the buttons, and if there's a winner, set the buttons where the player won to green for 1 second
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.buttons[i][0].config(background='green', activebackground="green")
                self.buttons[i][1].config(background='green', activebackground="green")
                self.buttons[i][2].config(background='green', activebackground="green")
                self.master.after(1000, lambda: self.reset_button_colors([(i, 0), (i, 1), (i, 2)]))
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                self.buttons[0][i].config(background='green', activebackground="green")
                self.buttons[1][i].config(background='green', activebackground="green")
                self.buttons[2][i].config(background='green', activebackground="green")
                self.master.after(1000, lambda: self.reset_button_colors([(0, i), (1, i), (2, i)]))
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.buttons[0][0].config(background='green', activebackground="green")
            self.buttons[1][1].config(background='green', activebackground="green")
            self.buttons[2][2].config(background='green', activebackground="green")
            self.master.after(1000, lambda: self.reset_button_colors([(0, 0), (1, 1), (2, 2)]))
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.buttons[0][2].config(background='green', activebackground="green")
            self.buttons[1][1].config(background='green', activebackground="green")
            self.buttons[2][0].config(background='green', activebackground="green")
            self.master.after(1000, lambda: self.reset_button_colors([(0, 2), (1, 1), (2, 0)]))
            return True
        return False

    def reset_button_colors(self, buttons):
        """Reset the color of the specified buttons to the default color."""
        for x, y in buttons:
            self.buttons[x][y].config(background='grey75', activebackground="grey75")
        self.reset()

    def check_tie(self) -> bool:
        """Check if the game's a tie."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def reset(self):
        """Reset the board."""
        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.master.title("Tic-Tac-Toe")