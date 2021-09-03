import random

class Game:
    def __init__(self, mode, boardSize, turn, board, currentX, currentO):
        self.mode = mode
        self.boardSize = boardSize
        self.turn = turn
        self.board = board
        self.currentX = currentX
        self.currentO = currentO

        

    def updateTurn(self):
        self.turn += 1

    def chooseRandomPlayer(self):
        return random.randint(1,2)
    
    def sendInput(self, row, column):
        print(f'Recived from {row},{column}')
        selectedSpace = self.board[row][column]
        print(f"Selected Space: {selectedSpace}")

        if selectedSpace == '': 
            selectedSpace = 'X' if self.turn % 2 != 0 else 'O'
            if self.turn % 2 != 0: 
                self.board[row][column] = 'X'
                self.currentX[row][column] = 'X'
            elif self.turn % 2 == 0:
                self.board[row][column] = 'O'
                self.currentO[row][column] = 'O'
        else: self.turn -= 1

    def computerMove(self):
        pass