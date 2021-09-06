import random
from tkinter import messagebox

class Game:
    def __init__(self, mode, boardSize, turn, board):
        self.mode = mode
        self.boardSize = boardSize
        self.turn = turn
        self.board = board
        self.gameOver = False
        self.winner = ''

    '''For Debug only (Remove later)'''
    def printBoardToConsole(self):
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                print(f'{self.board[row][col]} ', end='')
            print('\n')

    print('\n\n\n')

    def chooseRandomPlayer(self):
        return random.randint(1,2)
    
    def checkSpaces(self):
        #self.printBoardToConsole()

        '''Check Rows'''

        '''Check columns'''
        for row in range(self.boardSize):
                for col in range(self.boardSize):
                    
        '''Check Diagonals'''

        '''Check if board is completely filled'''
        if self.turn >= (self.boardSize ** 2): self.gameOver = True

    def sendInput(self, row, column):
        selectedSpace = self.board[row][column]

        if self.mode == 'm':
            if not self.gameOver:
                if selectedSpace == '-': 
                    selectedSpace = 'X' if self.turn % 2 == 0 or self.turn == 0 else 'O'
                    if self.turn % 2 == 0 or self.turn == 0: 
                        self.board[row][column] = 'X'
                    elif self.turn % 2 != 0:
                        self.board[row][column] = 'O'
                else: self.turn -= 1
                self.turn+=1
                self.checkSpaces()
            else:
                if self.winner != '':
                    messagebox.showinfo("Congratulations!", f"{self.winner} Won the Game")
                print("Game Done")

        elif self.mode == 's':
            
            self.checkSpaces()

            if self.turn % 2 != 0:
                if selectedSpace == '':
                    selectedSpace = 'X'
                    self.board[row][column] = 'X'
                    self.turn+=1
                    print(self.turn)
                    #if self.turn < (self.boardSize**2):
                    #    self.turn+=2
            elif self.turn % 2 == 0:
                self.computerMove()
                self.turn+=1

    def computerMove(self):
        placedSuccesfully = False
        while not placedSuccesfully:
            randRow = random.randint(0,self.boardSize-1)
            randCol = random.randint(0,self.boardSize-1)
            if self.board[randRow][randCol] == '':
                self.board[randRow][randCol] = 'O'
                placedSuccesfully = True