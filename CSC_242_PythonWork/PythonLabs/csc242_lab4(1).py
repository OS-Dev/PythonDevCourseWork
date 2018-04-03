from tkinter import Tk, Label, Entry, Button
from random import *
from tkinter import Frame,END
class Craps(Tk):

    #set up the main window
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Play Craps')
        self.new_game()
        self.make_widgets()

    #when a new game is started, the firstRoll will start at 0
    def new_game(self):
        self.firstRoll = 0
        
    #create and place the widgets in the window
    def make_widgets(self):
        Label(self, text="Die 1").grid(row=0, column=0, columnspan=1)
        Label(self, text="Die 2").grid(row=0, column=1, columnspan=1)

        self.die1Ent = Entry(self) #entry field for die 1
        self.die2Ent = Entry(self) #entry field for die 2
        self.die1Ent.grid(row=1, column=0, columnspan=1)
        self.die2Ent.grid(row=1, column=1, columnspan=1)

        Label(self, text="First roll").grid(row=2, column=0, columnspan=1)
        Label(self, text="Result").grid(row=2, column=1, columnspan=1)

        self.firstRollEnt = Entry(self) #entry field for the first roll
        self.resultEnt = Entry(self) #entry field the result of the current roll
        self.firstRollEnt.grid(row=3, column=0, columnspan=1)
        self.resultEnt.grid(row=3, column=1, columnspan=1)

        Button(self, text="Roll the dice!", command=self.play).grid(row=4, column=0)

    #complete the implementation of play()
    def play(self):
        import random
        self.die1Ent.delete(0,END)
        self.die2Ent.delete(0,END)
        self.resultEnt.delete(0,END)
        if self.firstRoll == 0:
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            self.firstRoll = d1+d2 
            self.firstRollEnt.insert(0,self.firstRoll)
            self.die1Ent.insert(0,d1)
            self.die2Ent.insert(0,d2)
            if self.firstRoll == 7 or 11:    
                self.resultEnt.insert(0,'You won! Play again?')
                Craps.new_game(self)
            elif firstRoll in [2,3,12]:
                self.resultEnt.insert(0,'You lost! Play again?')
                Craps.new_game(self)
            else:
                self.resultEnt.insert(0,'You need to roll again.')
        else:
            x = random.randint(1,6)
            y = random.randint(1,6)
            self.die1Ent.delete(0,END)
            self.die2Ent.delete(0,END)
            self.resultEnt.delete(0,END)           
            self.die1Ent.insert(0,x)
            self.die2Ent.insert(0,y)
            nextroll = x + y
            if nextroll == 7:    
                self.resultEnt.insert(0,'You lost! Play again?')
                Craps.new_game(self)
            elif nextroll == self.firstRoll:
                self.resultEnt.insert(0,'You won! Play again?')
                Craps.new_game(self)
            else:
                self.resultEnt.insert(0,'You need to roll again.')
Craps().mainloop()
