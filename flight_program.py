import tkinter
from tkinter import *
from tkinter import messagebox
import PIL as pillow
from PIL import Image, ImageTk


class MainWindowGUI:
   
    def __init__(self):

        #create Main window
        self.main_window = tkinter.Tk() #assigns mainwindow to master
        self.main_window.title(" TRENTON-BEDFORD SHUTTLE")
        self.main_window.minsize(width=700, height=200)
        self.main_window.resizable(False,False)

        self.main_window.columnconfigure(0, minsize =50)
        self.main_window.columnconfigure(1, minsize =100)
        self.main_window.columnconfigure(2, minsize =100)
        self.main_window.columnconfigure(3, minsize =100)
        self.main_window.columnconfigure(4, minsize =100)
        self.main_window.columnconfigure(5, minsize =100)
        self.main_window.columnconfigure(6, minsize =100)
        self.main_window.columnconfigure(7, minsize =50)

        #create heading label      
        self.heading_label = tkinter.Label(self.main_window,\
                                   text="Trenton-Bedford Shuttle",\
                                   font="helvetica,16", fg="blue")
        self.heading_label.grid(row=6, column=1, columnspan=6, rowspan=2,\
                                padx=35, pady=35)

        #store image 
        image = Image.open(r"C:\Users\Machi\Documents\School\RCBC\FALL 19\CSE 222\flight program\Plane1.jpg")
        photo = ImageTk.PhotoImage(image)
        
        #create label containing image
        self.labelJPG = Label(image = photo)
        self.labelJPG.image = photo
        self.labelJPG.grid(row=8, column=1, columnspan=6, rowspan=14)

        #create button widgets
        self.login_button = tkinter.Button(self.main_window,text="LOGIN",\
                                   font="helvetica,11", \
                                   command=self.login)
        self.login_button.grid(row=22, column=2, sticky=E, padx=5, pady=25)
       

        self.register_button = tkinter.Button(self.main_window,text="REGISTER",\
                                      font="helvetica,11",\
                                      command=self.register)
        self.register_button.grid(row=22, column=3,columnspan=2, padx=5, pady=25,\
                                  sticky=W)
        self.register_button.config(width=18)

        self.cancel_button = tkinter.Button(self.main_window,text="CANCEL",\
                                    font="helvetica,11",\
                                    command=self.main_window.destroy)
        self.cancel_button.grid(row=22, column=5,padx=5, pady=25,\
                                 sticky=E)
        self.cancel_button.config(width=10, height=1)

        tkinter.mainloop()

    def register(self):
        import createaccount
        
        RegisterAcctWin= createaccount.RegisterGUI()
        RegisterAcctWin.register_window.wait_window()
        self.register_button.config(state = DISABLED)
        self.login_button.config(state = NORMAL)
       
        
    def login(self):
        import login_Account
     
        LoginAcctWin= login_Account.LoginGUI()
        LoginAcctWin.login_window.wait_window()
        self.login_button.config(state = DISABLED)
        self.register_button.config(state = NORMAL)
        
        self.morph_window()
        
    def Price_info(self):
        #import ticket_price 

        #PriceInfoWin = ticket_price.PriceInfo_GUI()
        #PriceInfoWin.price_window.wait_window()
        self.price_window = tkinter.Tk()
        self.price_window.title("Price Information")
        self.price_window.minsize(width=350, height=200)
        
        try:
            infoFile = open('Price.txt', 'r')
            txt1 = infoFile.read()
            infoFile.close()
   
            priceS = txt1.split()
            orange_Time = priceS[21:24]
            print(orange_Time)
            print(orange_Time[2])

            black_Time = priceS[30:33]
            print(black_Time)
            print(black_Time[2])
            
            blue_Time = priceS[40:43]
            print(blue_Time)
            print(blue_Time[2])
            
            Textbox = tkinter.Text(self.price_window, height = 15, width = 120)
            Textbox.pack()

            Textbox.insert(END,txt1)
        except IOError:
            print('No file Exists.')

        infoFile.close()

    def selection_1(self, *args):
        print (self.option_var1.get())
        
        self.lblfrm = tkinter.LabelFrame(text = "Choose a Seat.", padx=3,\
                                         pady=3, bd=4, relief=SUNKEN)
        self.lblfrm.grid(row=10, rowspan=30, column=5, columnspan=2)#column=4
        aisle_list = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10',\
                      'L2','L3','L4','L5','L6','L7','L8','L9','L10']

        keyRow = 0
        keyCol = 0
        index = 0
        aisle_num = ""

        btn = list(range(len(aisle_list)))

        for aisle_num in aisle_list:
            
            cmd = lambda ale_num = aisle_num:self.button_clicked(ale_num, aisle_list)

            btn[index] = tkinter.Button(self.lblfrm, text = aisle_list[index],\
                                    font=("Helvetica",8), height=1, width=3, bd=3,\
                                    command=cmd)
            btn[index].grid(row=keyRow,column=keyCol)

            index = index +1
            keyCol = keyCol +1
            if keyCol >9:
                keyCol = 1
                keyRow = keyRow +1
                
    def button_clicked(self, ale_num, aisle_list):
        if ale_num == aisle_list[0]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[1]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[2]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[3]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[4]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[5]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[6]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[7]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[8]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[9]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[10]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[11]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[12]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[13]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[14]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[15]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[16]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[17]:
            print ("you have chosen " + str(ale_num))
            valid = True
        elif ale_num == aisle_list[18]:
            print ("you have chosen " + str(ale_num))
            valid = True
        else:
            valid = False
                                         
            
    def selection_2(self, *args):
        print (self.option_var2.get())
        self.lblfrm2 = tkinter.LabelFrame(text = "Choose a Seat.", padx=3,\
                                         pady=3, bd=4, relief=SUNKEN)
        self.lblfrm2.grid(row=42, rowspan=50, column=5, columnspan=2)#column=4
        aisle_list2 = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10',\
                      'L2','L3','L4','L5','L6','L7','L8','L9','L10']

        keyRow2 = 0
        keyCol2 = 0
        index2 = 0
        aisle_num2 = ""

        btn2 = list(range(len(aisle_list2)))

        for aisle_num2 in aisle_list2:
            cmd = lambda ale_num2 = aisle_list2:self.button2_clicked(ale_num2, aisle_list2)

            btn2[index2] = tkinter.Button(self.lblfrm2, text = aisle_list2[index2],\
                                    font=("Helvetica",8), height=1, width=3, bd=3,\
                                    command=cmd)
            btn2[index2].grid(row=keyRow2,column=keyCol2)

            index2 = index2 +1
            keyCol2 = keyCol2 +1
            if keyCol2 >9:
                keyCol2 = 1
                keyRow2 = keyRow2 +1
                
    def button2_clicked(self, ale_num2, aisle_list2):
        if ale_num2 == aisle_list2[0]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[1]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[2]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[3]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[4]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[5]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[6]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[7]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[8]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[9]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[10]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[11]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[12]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[13]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[14]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[15]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[16]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[17]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))
        elif ale_num2 == aisle_list2[18]:
            valid2 = True
            print ("you have chosen " + str(ale_num2))             
        else:
            valid2 = False
            
    def one_way(self):
        self.option_menu1.config(state = NORMAL)
        self.option_menu2.config(state = NORMAL)
        self.Twoway_button.config(state = DISABLED)
       
        
        if (valid == True):
            self.option_menu2.config(state = DISABLED)

        if (valid2 == True):          
            self.option_menu1.config(state = DISABLED)

        
    def two_way(self):
        self.Oneway_button.config(state = DISABLED)
        self.option_menu1.config(state = NORMAL)
        self.option_menu2.config(state = NORMAL)

    def clearAll(self):
        self.Oneway_button.config(state = NORMAL)
        self.Twoway_button.config(state = NORMAL)
        self.option_var1.set('Trenton - Bedford')
        self.option_menu1.config(state = DISABLED)
        self.lblfrm.grid_forget()
        self.option_var2.set('Bedford - Trenton')
        self.option_menu2.config(state = DISABLED)
        self.lblfrm2.grid_forget()
        
    def morph_window(self):
        print("inside the morph window")
        self.login_button.destroy()
        self.register_button.destroy()
        self.cancel_button.destroy()
        self.labelJPG.destroy()
        
        #resize window and heading
        
        self.main_window.minsize(width=700, height=300)
        self.heading_label.grid(row=5, column=1, columnspan=6, rowspan=2,\
                                padx=10, pady=15)
        #get the image
        photo = PhotoImage(file= "PlaneSeating3.gif")
        self.labelGIF =tkinter.Label(image=photo)
        self.labelGIF.image=photo    #retain a reference
        self.labelGIF.grid(row=8, column=1, columnspan=4, rowspan=100,\
                           padx=5, pady=5, sticky = W)
        self.PriceInfo_button = tkinter.Button(self.main_window,\
                                   text="Price Info",font="helvetica,11", \
                                   command=self.Price_info)
        self.PriceInfo_button.grid(row=5, column=1)
        self.selectFlight_label = tkinter.Label(self.main_window,\
                                   text="Select Flight",\
                                   font="helvetica,12", fg="black")
        self.selectFlight_label.grid(row=7, column=6,\
                                     padx=5, sticky=W)#column=5
        self.Purchase_button = tkinter.Button(self.main_window,\
                                   text="Purchase",font="helvetica,11")#, \
                                   #command=self.purchase)
        self.Purchase_button.grid(row=92, column=5, padx= 5, sticky=W)#column=6
        
        self.clearall_button = tkinter.Button(self.main_window,\
                                   text="Clear All Selections",font="helvetica,10", \
                                   command=self.clearAll)
        self.clearall_button.grid(row=92, column=6, padx= 5, sticky=W)#column=7
       
        self.Oneway_button = tkinter.Button(self.main_window,\
                                   text="One-Way ticket",font="helvetica,11", \
                                   command = self.one_way)
        self.Oneway_button.grid(row=7, column=4, padx= 5, sticky=W)#row=7, column=7
        
        self.Twoway_button = tkinter.Button(self.main_window,\
                                   text="Two-Way ticket",font="helvetica,11", \
                                   command=self.two_way)
        self.Twoway_button.grid(row=8, column=4, padx= 5, sticky=W)#row=8, column=7,

        #menu options for trenton to Bedford
        optionList1 = ('7:00 AM', '9:00 AM', '1:00 PM', '3:00 PM')
        self.option_var1=tkinter.StringVar()
        self.option_var1.set('Trenton - Bedford')
        self.option_menu1 = tkinter.OptionMenu(self.main_window,self.option_var1,\
                                          *optionList1, command = self.selection_1)
        self.option_menu1.grid(row=9, column=6,sticky=W)#row=9, column=5
        self.option_menu1.config(state = DISABLED)
        
        #menu options for bedford to trenton
        optionList2 = ('8:00 AM', '10:00 AM', '2:00 PM', '4:00 PM')
        self.option_var2=tkinter.StringVar()
        self.option_var2.set('Bedford - Trenton')
        self.option_menu2 = tkinter.OptionMenu(self.main_window,self.option_var2,\
                                          *optionList2, command = self.selection_2)
        self.option_menu2.grid(row=41, column=6,sticky=W)#column=5
        self.option_menu2.config(state = DISABLED)
    
        
    #def on_closing():
       # if 
        
#create an instance of the class
main_Gui = MainWindowGUI()

        
