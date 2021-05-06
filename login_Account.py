import tkinter
from tkinter import *
from tkinter import messagebox
import re


class LoginGUI:

    def __init__(log):
        print("In LoginGUI")
        
        log.login_window = tkinter.Tk()
        log.login_window.title("Login")
        log.login_window.minsize(width=350, height=200)

        log.login_window.columnconfigure(0, minsize =25)
        log.login_window.columnconfigure(1, minsize =50)
        log.login_window.columnconfigure(2, minsize =50)
        log.login_window.columnconfigure(3, minsize =50)
        log.login_window.columnconfigure(4, minsize =50)
        log.login_window.columnconfigure(5, minsize =50)
        log.login_window.columnconfigure(6, minsize =50)
        log.login_window.columnconfigure(7, minsize =25)
        
        log.username_label = tkinter.Label(log.login_window,text="Username:")
        log.username_label.grid(row=2,  column=1, columnspan=2, sticky=E, pady=15, padx=10)
        
        log.password_label = tkinter.Label(log.login_window,text="Password:")
        log.password_label.grid(row=3, column=1, columnspan=2, sticky=E, pady=15, padx=10)

        log.username_Entry = tkinter.Entry(log.login_window,width=15, justify='right',\
                                    font=("helvetica",10))
        log.username_Entry.grid(row=2, column=3, columnspan=2, sticky=W)
        log.username_Entry.focus_force()
        
        log.password_Entry = tkinter.Entry(log.login_window,width=15, justify='right',\
                                    font=("helvetica",10),show='*')
        log.password_Entry.grid(row=3, column=3, columnspan=2, sticky=W)
        log.password_Entry.bind("<Return>", log.verify_userName)
        
        log.login_button = tkinter.Button(log.login_window,text="LOGIN",\
                                  font=("Helvetica",10), command=log.verify_userName)
        log.login_button.grid(row=4, column=2, sticky=E, padx=10)
        log.login_button.config(width=20, height=1)
     
    #function identifies user
    def verify_userName(log, event=None):

        valid = True

        Username = log.username_Entry.get()    #get the entry
        print ('Username is: '+ Username + '\n')
        cnt =0
        
        try:
            userDataFile = open('acct_user_names.txt', 'r')     # open file to read

            
            #loop line by line to check the values
            for userTemp in userDataFile:
                cnt +=1
                
                print('userTemp from file is: ' + userTemp)
                if Username == userTemp.rstrip():
                    valid = True
                    count =cnt
                    break
                
                else:
                    valid= False
                                      
                               
            userDataFile.close()
           
            
            if (valid == False):     #if it doesn't exists in the file
                tkinter.messagebox.showinfo('Login Fail','Invalid Username or Password\n Please try again')
                print('Invalid User Name')
                log.username_Entry.delete(0,END)
                log.username_Entry.focus_force()    #give it the focus
                log.password_Entry.delete(0,END)
                log.login_window.lift()
                
            else:   #in the file....verify pass and send the username to write if pass is good
                log.verify_Password(count)
        
        except IOError:
            print('No file Exists.')
        
        

    #function verifies correct password        
    def verify_Password(log, count):
        
        print ("In the verify password function")
        valid = True
        
        Password = log.password_Entry.get()    #get the entry
        print ('Password is: '+ Password + '\n')

        passwordFile = open('acct_user_passwords.txt', 'r')

        #loop line by line to check the values
        i =0
        for passTemp in passwordFile:
            i += 1
            print('passTemp from file is: ' + passTemp)
            if (i != count or Password != passTemp.rstrip()):
                valid = False
                                
            else :
                valid =True
                break
                                
        passwordFile.close()

            
        if (valid == False):     #if it exists in the file
            print('Invalid Username or Password')
            tkinter.messagebox.showinfo('Login Fail','Invalid Username or Password\n Please try again')
            log.username_Entry.delete(0,END)
            log.username_Entry.focus_force()    #give it the focus
            log.password_Entry.delete(0,END)
            log.login_window.lift()

        else: #this will direct you back to main
            log.end_login()
        
                  
    def end_login(log):
        print("inside the end login window")
        
        tkinter.messagebox.showinfo('Login Successful','You have successfully logged in.')
        log.username_Entry.delete(0,END)
        log.password_Entry.delete(0,END)
        log.login_window.destroy()
      
        

       
