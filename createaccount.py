import tkinter
from tkinter import *
from tkinter import messagebox
import re

class RegisterGUI:

    def __init__(reg):
        print("In RegisterGUI")
        reg.register_window = tkinter.Tk()
        reg.register_window.title(" Account Registration")
        reg.register_window.minsize(width=350, height=200)

        #creates username label
        reg.username_label = tkinter.Label(reg.register_window,text="Username:")
        reg.username_label.grid(row=1, column=1, columnspan=2, sticky=W, pady=15, padx=10)

        #creates password info label indicates criteria for password
        reg.passInfo_label = tkinter.Label(reg.register_window,text="Create a password of at least nine (9) characters,\nthat contains at leas one digit, one uppercase,\nand one lowercase letter")
        reg.passInfo_label.grid(row=2, column=1, columnspan=4, sticky=W+E, pady=15, padx=10)

        #creates password label
        reg.password_label = tkinter.Label(reg.register_window,text="Password:")
        reg.password_label.grid(row=3, column=1, columnspan=2, sticky=W, pady=15, padx=10)

        #username variable to store user input
        reg.userName_entry = tkinter.Entry(reg.register_window,width=15, justify='right',\
                                    font=("helvetica",10))
        reg.userName_entry.grid(row=1, column=3, columnspan=2, sticky=W)
        reg.userName_entry.focus_force()

        #password variable to store user input
        reg.password_entry = tkinter.Entry(reg.register_window,width=15, justify='right',\
                                    font=("helvetica",10),show='*')
        reg.password_entry.grid(row=3, column=3, columnspan=2, sticky=W)
        reg.password_entry.bind("<Return>", reg.verify_userName)

        #creates button
        reg.register_button = tkinter.Button(reg.register_window,text="REGISTER ACCOUNT",\
                                  font=("Helvetica",10), command=reg.verify_userName)
        reg.register_button.grid(row=4, column=2, sticky=E, padx=10)
        reg.register_button.config(width=20, height=1)
        
        reg.cancel_button = tkinter.Button(reg.register_window,text="CANCEL",\
                                  font=("Helvetica",10),command=reg.register_window.destroy)
        reg.cancel_button.grid(row=4, column=3,padx=10, sticky=E)
        reg.cancel_button.config(width=10, height=1)

    #function validates username
    def verify_userName(reg, event=None):
        valid = True
        newUser = reg.userName_entry.get()    #get the entry
        print ('newUser is: '+ newUser + '\n')

        try:
            userDataFile = open('acct_user_names.txt', 'r')     # open file to read

            #loop line by line to check the values
            for userTemp in userDataFile:
                print('userTemp from file is: ' + userTemp)
                if newUser == userTemp.rstrip():
                    valid = False
            userDataFile.close()

            if (valid == False):     #if it exists in the file
                tkinter.messagebox.showinfo('Invalid User Name','That User Name already exists.')
                reg.userName_entry.delete(0,END)
                reg.userName_entry.focus_force()    #give it the focus
                reg.register_window.lift()

            else:   #not in the file....verify pass and send the username to write if pass is good
                reg.verify_newPassword(newUser)

        except IOError:
            print('No file Exists!')
            userDataFile = open('acct_user_names.txt', 'w+')     # creates file to write to
            print('File acct_user_names.txt has now been created!')

    #Function creates password 
    def verify_newPassword(reg, user):
       
        txt = reg.password_entry.get()   #get the password entry
        print('Getting password   ' + txt)
        
        if reg.verify_Password(txt):    #if the call to verify password criteria is met
            userFile = open('acct_user_names.txt', 'a') #open the user file to append it
            userFile.write(user + '\n')     #add the password to the file 
            userFile.close()

            passwordFile = open('acct_user_passwords.txt', 'a')
            passwordFile.write(txt + '\n')
            passwordFile.close()
            tkinter.messagebox.showinfo('Account Creation','Account successfully created.')
            reg.register_window.lift()
            reg.register_window.destroy()

        else:
            tkinter.messagebox.showinfo('Password Validation', '"' + txt + '"' + ' is not a valid passowrd')        
            reg.password_entry.delete(0,END)
            reg.password_entry.focus_force()    #give it the focus
            reg.register_window.lift()
            
    #Function to validate the password           
    def verify_Password(reg, txt):
        
        valid = True
        
        if (len(txt)<9):
            valid = False
            tkinter.messagebox.showinfo("Password Validation: Length","Create a password 9 characters or more in length")
             
        elif not re.search("[a-z]", txt): 
            valid = False
            tkinter.messagebox.showinfo("Password Validation: Lowercase Charaters","Create a password that contains at least one lower case letter")
            
        elif not re.search("[A-Z]", txt): 
            tkinter.messagebox.showinfo("Password Validation: Uppercase Charaters","Create a password that contains at least one upper case letter")
            
        elif not re.search("[0-9]", txt): 
            valid = False
            tkinter.messagebox.showinfo("Password Validation: Numbers","Create a password that contains at least one digit")
                          
        else:
            valid = True
            tkinter.messagebox.showinfo("Password Validation:","Valid password")
            
        return valid

