from tkinter import *
from tkinter import messagebox
from Game import Game

global game

root = Tk()
root.title("Tic Tac Toe")
turnLabelTxt = StringVar()
turnLabelTxt.set(f"Current Turn: X")

btnGridSize = 4

class Gui:
    def __init__(self):
        pass
            
    def MainMenu(self):
        self.clearWindow(self)
        titleBtnWidth, titleBtnHeight = 20, 2
        Label(root, text="Tic Tac Toe", font=("20")).grid(row=0,column=0, sticky='N')
        Button(root, text="Single Player", width=titleBtnWidth, height=titleBtnHeight, command=lambda: self.boardSizeScreen(self, 's')).grid(row=1, column=0, sticky='N')
        Button(root, text="Multiplayer",  width=titleBtnWidth, height=titleBtnHeight, command=lambda: self.boardSizeScreen(self, 'm')).grid(row=2, column=0, sticky='N')
        Button(root, text="Exit", width=titleBtnWidth, height=titleBtnHeight, command=lambda:exit()).grid(row=3, column=0, sticky='N')

        root.mainloop()

    def gameOverScreen(self):
        global game
        self.clearWindow(self)

        if game.winner != '':
            Label(root, text = f"{game.winner}: Wins!").grid(row=0, column=0, columnspan=2)
        else:
            Label(root, text = "The game ended in a draw").grid(row=0, column=0, columnspan=2)
        Button(root, text="Play Again", command=lambda: self.MainMenu(self)).grid(row=1, column=0)
        Button(root, text="Exit", command=exit).grid(row=1, column=1)

    def click(self, row, column):
        global game
        game.sendInput(row, column)

        if game.gameOver:
            self.gameOverScreen(self)
        else:
            turnLabelTxt.set(f"Current Turn: {'X' if game.turn % 2 == 0 or game.turn == 0 else 'O'}")
            self.gameScreen(self)

    def gameScreen(self):
        global game
        self.clearWindow(self)
        #Button(root, text='-', width=btnGridSize*3, height=btnGridSize).grid(row=0, column=0)
        Label(root, text=turnLabelTxt.get(), font="24").grid(row=0, column=0, columnspan=game.boardSize)       
        buttonList = [[] for i in range(game.boardSize)]
        for currentRow in range(game.boardSize):
            for currentColumn in range(game.boardSize):
                buttonList[currentRow].append(Button(root, text=game.board[currentRow][currentColumn], width=btnGridSize*3, height=btnGridSize))

                buttonList[currentRow][currentColumn].config(command=lambda row=currentRow, column=currentColumn: self.click(self, row, column))
                buttonList[currentRow][currentColumn].grid(row=currentRow+1, column=currentColumn)
                #buttonList[currentRow][currentColumn] = Button(buttonFrame, text='-', width=btnGridSize*3, height=btnGridSize).grid(row=currentRow, column=currentColumn)        

    def updateBoardSize(self, boardSizeInput, mode):
        global game
        updatedSize = int(boardSizeInput)
        if updatedSize % 2 == 1 and updatedSize > 2 and updatedSize < 10:
                gameBoard = [['' for i in range(updatedSize)] for row in range(updatedSize)]
                game = Game(mode, updatedSize, 0, gameBoard)
                #messagebox.showinfo("Sucess", f"Gameboard set to {updatedSize}x{updatedSize}")
                self.gameScreen(self)
        else:
            messagebox.showerror("Input Error", "Invalid Board input\nPlease input an odd number betweek 3 and 9")
            self.boardSizeScreen(self)
            
            
    def boardSizeScreen(self, mode):
        self.clearWindow(self)

        boardSizeInput = StringVar()
        Label(root, text="Board size: ").grid(row=0, column=0)
        Entry(root, textvariable=boardSizeInput).grid(row=0, column=1)
        Button(root, text="Set Board Size", command=lambda: self.updateBoardSize(self, boardSizeInput.get(), mode)).grid(row=1, column=0, columnspan=2)

    def clearWindow(self):
        for widget in root.winfo_children():
            widget.destroy()