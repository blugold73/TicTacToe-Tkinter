import random

class Game:
    def __init__(self, mode, boardSize, turn, board):
        self.mode = mode
        self.boardSize = boardSize
        self.turn = turn
        self.board = board
        self.gameOver = False
        self.winner = ''

    def checkSpaces(self):
        print(f'Board: {self.board}')
        print(f'Turn: {self.turn}')

        '''Check Rows'''
        for i in range(self.boardSize):
            rowStr = ''.join(self.board[i][:self.boardSize])

            if rowStr == 'X'*self.boardSize:
                self.winner = 'X'
                self.gameOver = True
            if rowStr == 'O'*self.boardSize:
                self.winner = 'O'
                self.gameOver = True

        '''Check Columns'''
        for i in range(self.boardSize):
            colStr = ''
            for j in range(self.boardSize):
                colStr += self.board[j][i]

            if colStr == 'X'*self.boardSize:
                self.winner = 'X'
                self.gameOver = True
            if colStr == 'O'*self.boardSize:
                self.winner = 'O'
                self.gameOver = True

        '''Check Diagonals'''
        diagonalDown, diagonalUp = '', ''
        for i in range(self.boardSize):
            diagonalDown += self.board[i][i]
            diagonalUp += self.board[self.boardSize-1-i][i]

        if diagonalUp == 'X'*self.boardSize or diagonalDown == 'X'*self.boardSize:
            self.winner = 'X'
            self.gameOver = True
            
        if diagonalUp == 'O'*self.boardSize or diagonalDown == 'O'*self.boardSize:
            self.winner = 'O'
            self.gameOver = True
        '''Check if board is completely filled'''
        if self.turn == (self.boardSize ** 2): self.gameOver = True

    def sendInput(self, row, column):
        #print(f'Recived from {row},{column}')
        selectedSpace = self.board[row][column]
        #print(f"Selected Space: {selectedSpace}")

        if self.mode == 'm': #Multiplayer function
            if not self.gameOver:
                if selectedSpace == '':
                    #decides which player just made the turn
                    selectedSpace = 'X' if self.turn % 2 == 0 or self.turn == 0 else 'O'
                    if self.turn % 2 == 0 or self.turn == 0: 
                        self.board[row][column] = 'X'
                    elif self.turn % 2 != 0:
                        self.board[row][column] = 'O'
                else: self.turn -= 1
                self.turn+=1
                self.checkSpaces()

        elif self.mode == 's': #Singleplayer function
            if not self.gameOver:
                if selectedSpace == '': 
                    #decides which player just made the turn
                    selectedSpace = 'X' if self.turn % 2 == 0 or self.turn == 0 else 'O'
                    if self.turn % 2 == 0 or self.turn == 0: 
                        self.board[row][column] = 'X'
                        self.turn+=1
                    self.checkSpaces()
                    
                    if not self.gameOver:
                        self.computerMove()
                        self.checkSpaces()
                else: self.turn -= 1

    def computerMove(self):
        placedSuccesfully = False
        while not placedSuccesfully:
            randRow = random.randint(0,self.boardSize-1)
            randCol = random.randint(0,self.boardSize-1)
            if self.board[randRow][randCol] == '':
                self.board[randRow][randCol] = 'O'
                placedSuccesfully = True
                self.turn+=1