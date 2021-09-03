from tkinter import *
from Game import Game

root = Tk()
root.title("Tic Tac Toe")
game = Game()

class Gui:
    def __init__(self):
        pass
            
    def MainMenu(self):
        #root.geometry('150x150')
        titleBtnWidth, titleBtnHeight = 20, 2
        Label(root, text="Tic Tac Toe", font=("20")).grid(row=0,column=0, sticky='N')
        Button(root, text="Single Player", width=titleBtnWidth, height=titleBtnHeight, command=game.playSingle).grid(row=1, column=0, sticky='N')
        Button(root, text="Multiplayer",  width=titleBtnWidth, height=titleBtnHeight, command=game.playMulti).grid(row=2, column=0, sticky='N')
        Button(root, text="Exit", width=titleBtnWidth, height=titleBtnHeight, command=lambda:exit()).grid(row=3, column=0, sticky='N')

        root.mainloop()
    def clearWindow(self):
        for widget in root.winfo_children:
            widget.destory()