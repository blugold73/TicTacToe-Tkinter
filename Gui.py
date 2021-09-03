from tkinter import *
from tkinter import messagebox
from Game import Game

root = Tk()
root.title("Tic Tac Toe")
game = Game('u', 0, [])

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

    def click(self):
        pass

    def gameScreen(self):
        btnGridSize = 4
        playerOne, playerTwo = 'X', 'O'
        coinFlip, firstTurn = game.chooseRandomPlayer(), ''
        if coinFlip == 0: firstTurn = playerOne
        elif coinFlip == 1: firstTurn = playerTwo

        self.clearWindow(self)
        #Button(root, text='-', width=btnGridSize*3, height=btnGridSize).grid(row=0, column=0)

        Label(root, text=f"Current Turn: {firstTurn}", font="24").grid(row=0, column=0, columnspan=game.boardSize)       
        print(game.boardSize)
        buttonList = [[] for i in range(game.boardSize)]
        print(buttonList)
        for currentRow in range(game.boardSize):
            for currentColumn in range(game.boardSize):
                buttonList[currentRow].append(Button(root, width=btnGridSize*3, height=btnGridSize))

                buttonList[currentRow][currentColumn].config(command=lambda row=currentRow, column=currentColumn: click(row,column))
                buttonList[currentRow][currentColumn].grid(row=currentRow+1, column=currentColumn)
                #buttonList[currentRow][currentColumn] = Button(buttonFrame, text='-', width=btnGridSize*3, height=btnGridSize).grid(row=currentRow, column=currentColumn)

        if game.mode == 's':
            pass
        elif game.mode == 'm':
            pass

        print("Playing Game")

    def setupGame(self, mode):
        game.mode = mode
        self.boardSizeScreen(self)
        

    def updateBoardSize(self, boardSizeInput):
        updatedSize = int(boardSizeInput)
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

        boardSizeInput = StringVar()
        Label(root, text="Board size: ").grid(row=0, column=0)
        Entry(root, textvariable=boardSizeInput).grid(row=0, column=1)
        Button(root, text="Set Board Size", command=lambda: self.updateBoardSize(self, boardSizeInput.get())).grid(row=1, column=0, columnspan=2)

    def clearWindow(self):
        for widget in root.winfo_children():
            widget.destroy()