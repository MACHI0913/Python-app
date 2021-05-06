import tkinter
from tkinter import *
from tkinter import messagebox

class PriceInfo_GUI:

    def __init__(pri):
        print("In TicketGUI")

        pri.price_window = tkinter.Tk()
        pri.price_window.title("Price Information")
        pri.price_window.minsize(width=350, height=200)
        
        try:
            infoFile = open('Price.txt', 'r')
            txt1 = infoFile.read()
            infoFile.close()

            for word in txt1.split():
                print(word) #prints each word vertically test purposes
            txt1 [10]
            #with open('Price.txt', 'r') as infoFile:
                #for line in infoFile:
                    #txt1.extend(line.split())
                            
                

            Textbox = tkinter.Text(pri.price_window, height = 15, width = 120)
            Textbox.pack()

            Textbox.insert(END,txt1)
        except IOError:
            print('No file Exists.')

        infoFile.close()
