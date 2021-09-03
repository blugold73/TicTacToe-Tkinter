from tkinter import *
from tkinter import messagebox
from Game import Game

root = Tk()
root.title("Tic Tac Toe")
game = Game('u', 0, [])
boardSizeInput = StringVar()

class Gui:
    def __init__(self):
        pass
            
    def MainMenu(self):
        titleBtnWidth, titleBtnHeight = 20, 2
        Label(root, text="Tic Tac Toe", font=("20")).grid(row=0,column=0, sticky='N')
        Button(root, text="Single Player", width=titleBtnWidth, height=titleBtnHeight, command=lambda: self.setupGame(self, 's')).grid(row=1, column=0, sticky='N')
        Button(root, text="Multiplayer",  width=titleBtnWidth, height=titleBtnHeight, command=lambda: self.setupGame(self, 'm')).grid(row=2, column=0, sticky='N')
        Button(root, text="Exit", width=titleBtnWidth, height=titleBtnHeight, command=lambda:exit()).grid(row=3, column=0, sticky='N')

        root.mainloop()

    def gameScreen(self):
        self.clearWindow(self)
        print("Playing Game")

    def setupGame(self, mode):
        if mode == 's': game.mode = 's'
        if mode == 'm': game.mode = 'm'
        self.boardSizeScreen(self)
        

    def updateBoardSize(self):
        updatedSize = int(boardSizeInput.get())
        if updatedSize % 2 == 1 and updatedSize > 2 and updatedSize < 10:
                game.boardSize = updatedSize
                gameBoard = [['' for i in range(updatedSize)] for row in range(updatedSize)]
                game.board = gameBoard
                messagebox.showinfo("Sucess", f"Gameboard set to {updatedSize}x{updatedSize}")
                self.gameScreen(self)
        else:
            messagebox.showerror("Input Error", "Invalid Board input\nPlease input an odd number betweek 3 and 9")
            self.boardSizeScreen(self)
            
            
    def boardSizeScreen(self):
        self.clearWindow(self)

        Label(root, text="Board size: ").grid(row=0, column=0)
        Entry(root, textvariable=boardSizeInput).grid(row=0, column=1)
        Button(root, text="Set Board Size", command=lambda: self.updateBoardSize(self)).grid(row=1, column=0, columnspan=2)

    def clearWindow(self):
        for widget in root.winfo_children():
            widget.destroy()