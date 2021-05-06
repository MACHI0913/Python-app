import tkinter
from tkinter import *


class back_to_main:
    
    def __init__(back,self):
        print("in back to main module")
        back.bk_window=self
        back.bk_window.destroy()
       
        back.call_main()
    
    def call_main(self):
        print("in function")
        import flight_program 

        FPwindow = flight_program()
        FPwindow.login_button.destroy()
    
    
root = Tk()

Back = back_to_main(root)
root.mainloop()
