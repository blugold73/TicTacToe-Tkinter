import random

class Game:
    def __init__(self, mode, boardSize, board, turn):
        self.mode = mode
        self.boardSize = boardSize
        self.board = board
        self.turn = turn

    def updateTurn(self):
        self.turn += 1

    def chooseRandomPlayer(self):
        return random.randint(1,2)
    
    def sendInput(self, row, column):
        print(f'Recived from {row},{column}')

    def computerMove(self):
        pass