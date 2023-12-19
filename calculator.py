import tkinter as tk
from settings import *

class Calulator(tk.Tk):
    def __init__(self,title,size):
       # main setup of application(calculator)
       # here will account fro geometry and and size 
        super().__init__()
        self.title(title)
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False,False)
        self.minsize(size[0],size[1])
        

        #grid layout 
        self.rowconfigure(list(range(MAIN_ROWS)),weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMN)),weight=1, uniform='a')
        # widgets 
        self.create_widgets()

        self.mainloop()
    def create_widgets(self):
        main_font = tk.Tk(family = FONT, size = NORMAL_FONT_SIZE)
        result_fonts = tk.Tk(family = FONT, size = OUTPUT_FONT_SIZE)
    
        OutputLabel(self, row=0, anchor='SE',font= main_font)   # formula
        OutputLabel(self, row=1, anchor='E', font=result_fonts)    # result

class OutputLabel(tk.Label):
    def __init__(self, parent, row, anchor):
        super().__init__(master=parent, text=123)
        self.grid(column=0, columnspan=4, row=row, sticky= anchor)

if __name__ == '__main__':
  Calulator('calculator', (400,600))
        
        