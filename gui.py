#!/usr/bin/python

import Tkinter as tk
import core

class CalculatorApp(tk.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=500, bg="BLACK")
        # Set the title
        self.master.title('PyCalculator')
        self.master.configure(background='black')
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        self.calc = core.Calculator()
        self.master.bind('<KeyPress>', self.onKeyPress)
        self.master.bind('<Enter>', self.evaluate)
        self.master.bind('<Return>', self.evaluate)
        # We'll use the flexible pack layout manager
        self.pack()
    
        self.display = tk.Label(self, text="0", justify="right", font=("Raleway", 30))
        self.display.pack(fill=tk.X, side=tk.TOP)

        for i in range(1,10):
          #btn = tk.Button(self, text=i, command=self.add(i))
          button = tk.Button(master=self, text=i, command= lambda: self.add(i), font=("Raleway", 16))

          button.pack(fill=tk.X, side=tk.TOP)

        clearBtn = tk.Button(self, text="C", command=self.clear())
        clearBtn.pack(fill=tk.X, side=tk.TOP)

        
        #self.recipient.pack(fill=tk.X, side=tk.TOP)
    def onKeyPress(self,event):
      if (event.char.isdigit()):
        self.add(int(event.char))
      elif event.char in {'+', "-", "/", "*"}:
        self.calc.operate(event.char)
      elif event.char == "=":
        self.evaluate('wtf')
      elif event.char == "c":
        self.clear()


    def evaluate(self, wtf):
      #print(self.calc.evaluate())
      self.setDisplay(self.calc.evaluate())

    def setDisplay(self, value):
      self.display.config(
        text=value
      )
    def run(self):
        ''' Run the app '''
        self.mainloop()

    def add(self, value):
      self.calc.add(value)
      self.display.text = str(self.calc.getValue())
      self.setDisplay(self.calc.getValue())

    def clear(self):
      self.calc.clear()
      self.setDisplay("0")



def init():
  app = CalculatorApp(tk.Tk())
  app.run()