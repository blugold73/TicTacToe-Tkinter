import random

class Game:
    def __init__(self, mode, boardSize, board):
        self.mode = mode
        self.boardSize = boardSize
        self.board = board

    def chooseRandomPlayer(self):
        return random.randint(0,1)
    
    def sendInput(self, row, column):
        print(f'Recived from {row},{column}')