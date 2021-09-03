import random

class Game:
    def __init__(self, mode, boardSize, turn, board, currentX, currentO):
        self.mode = mode
        self.boardSize = boardSize
        self.turn = turn
        self.board = board
        self.currentX = currentX
        self.currentO = currentO

    def chooseRandomPlayer(self):
        return random.randint(1,2)
    
    def sendInput(self, row, column):
        print(f'Recived from {row},{column}')
        selectedSpace = self.board[row][column]
        print(f"Selected Space: {selectedSpace}")

        if self.mode == 'm':   
            if selectedSpace == '': 
                selectedSpace = 'X' if self.turn % 2 != 0 else 'O'
                if self.turn % 2 != 0: 
                    self.board[row][column] = 'X'
                    self.currentX[row][column] = 'X'
                elif self.turn % 2 == 0:
                    self.board[row][column] = 'O'
                    self.currentO[row][column] = 'O'
            else: self.turn -= 1
        elif self.mode == 's':
            if self.turn % 2 != 0:
                if selectedSpace == '':
                    print(self.turn)
                    selectedSpace = 'X'
                    self.board[row][column] = 'X'
                    self.computerMove()
                    if self.turn < self.boardSize**2:
                        self.turn+=2
                    elif self.turn == (self.boardSize**2):
                        print("Final move of game")
        print(self.currentX)
        print(self.currentO)

    def computerMove(self):
        placedSuccesfully = False
        while not placedSuccesfully:
            randRow = random.randint(0,self.boardSize-1)
            randCol = random.randint(0,self.boardSize-1)
            if self.board[randRow][randCol] == '':
                self.board[randRow][randCol] = 'O'
                self.currentO[randRow][randCol] = 'O'
                placedSuccesfully = True