from tkinter import *
import random

class DecisionMaker(Frame):

    def __init__(self):
        """sets up frame and widgets"""
        Frame.__init__(self)
        self.master.title("Decision Maker")
        self.grid()

        #Create label and field for decision 1
        self._decision1Label = Label(self, text = "Option 1")
        self._decision1Label.grid(row = 0, column = 0)

        self._decision2Label = Label(self, text = "Option 2")
        self._decision2Label.grid(row = 1, column = 0)

        #Option 1 text box entry
        self.dec1Var = StringVar()
        self.dec1Entry = Entry(self,
                               textvariable = self.dec1Var)
        self.dec1Entry.grid(row = 0, column = 1, columnspan = 2)

        #Option 2 text box entry
        self.dec2Var = StringVar()
        self.dec2Entry = Entry(self,
                               textvariable = self.dec2Var)
        self.dec2Entry.grid(row = 1, column = 1, columnspan = 2)

        #answer box
        self.answer = Label(self, text = "")
        self.answer.grid(row = 3, column = 0, columnspan = 3)
        #Command button
        self.choiceButton = Button(self,
                                   text = "Choose",
                                   command = self.choice)
        self.choiceButton.grid(row = 2, column = 0, columnspan = 3)

    def choice(self):
        """chooses between the two options"""
        option1 = self.dec1Var.get()
        option2 = self.dec2Var.get()
        optionlist = [option1, option2]
        choice = random.choice(optionlist)
        self.answer['text'] = choice
        
        
        



def main():
    DecisionMaker().mainloop()

main()
