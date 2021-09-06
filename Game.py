import random

class Game:
    def __init__(self, mode, boardSize, turn, board, currentX, currentO):
        self.mode = mode
        self.boardSize = boardSize
        self.turn = turn
        self.board = board
        self.currentX = currentX
        self.currentO = currentO
        self.gameOver = False

    def chooseRandomPlayer(self):
        return random.randint(1,2)
    
    def checkSpaces(self):
        print(f'Board: {self.board}')
        print(f'BoardX: {self.currentX}')
        print(f'BoardO: {self.currentO}')
        print(f'Turn: {self.turn}')

        '''Check Rows'''

        '''Check Columns'''

        '''Check Diagonals'''

        '''Check if board is completely filled'''
        if self.turn >= (self.boardSize ** 2): self.gameOver = True

    def sendInput(self, row, column):
        print(f'Recived from {row},{column}')
        selectedSpace = self.board[row][column]
        print(f"Selected Space: {selectedSpace}")

        if self.mode == 'm':
            if not self.gameOver:
                if selectedSpace == '': 
                    selectedSpace = 'X' if self.turn % 2 == 0 or self.turn == 0 else 'O'
                    if self.turn % 2 == 0 or self.turn == 0: 
                        self.board[row][column] = 'X'
                        self.currentX[row][column] = 'X'
                    elif self.turn % 2 != 0:
                        self.board[row][column] = 'O'
                        self.currentO[row][column] = 'O'
                else: self.turn -= 1
                self.turn+=1
                self.checkSpaces()
            else:
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
                self.currentO[randRow][randCol] = 'O'
                placedSuccesfully = True