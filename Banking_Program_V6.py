# Importing neccessary modules
from tkinter import *
import sys
import time
import os


Icon_PATH = str(os.path.abspath("bankicon.ico"))
Icon_PATH = Icon_PATH.replace("\\", "/")

filename_cont = 0

root = Tk()

root.iconbitmap(Icon_PATH)

root.title("New Age Bank")

# Creating Customer Class
class Customer:
    def __init__(self, first, last, number, balance, username, password):
        self.first = first
        self.last = last
        self.number = number
        self.balance = balance
        self.username = username
        self.password = password

    def open_files(self):
        global filename2
        global filename_cont
        global filename
        global where_to
        where_to = self.username
        if where_to == ahanj.username:
            where_to = ahanj
        if where_to == bobs.username:
            where_to = bobs
        if where_to == michaelj.username:
            where_to = michaelj
        
        filename = self.username + '.txt'
        filename2 = open(filename, 'r+')
        filename_cont = filename2.read()
        self.balance = filename_cont


# Creating homescreen method
    def homescreen(self):
        self.open_files()
        global balance_label
        global make_depo_but
        global make_with_but
        global see_details_but
        global exit_but
        global logout_but
        see_details_but = Button(root, text='See Account Details', font=('Helvetica', 13),  padx=4, command=lambda: self.see_details())
        balance_label = Label(root, text="Balance is: $" + str(self.balance), font=('Helvetica', 13))
        make_depo_but = Button(root, text="Make Deposit", font=('Helvetica', 13), padx=20, command=lambda: self.deposit_win())
        make_with_but = Button(root, text="Make Withdrawl", font=('Helvetica', 13), padx=13, command=lambda: self.withdrawl_win())
        exit_but = Button(root, text="Exit", padx=46, font=('Helvetica', 13), command=lambda: exit_program(1))
        logout_but = Button(root, text="Log Out", font=('Helvetica', 13), padx=34, command=lambda: exit_program(2)) 
        balance_label.grid(row=0, column=0)
        make_depo_but.grid(row=1, column=0)
        make_with_but.grid(row=2, column=0)
        see_details_but.grid(row=3, column=0)
        exit_but.grid(row=5, column=0)
        logout_but.grid(row=4, column=0)

# Creating a method allowing to see account details
    def see_details(self):
        global first_label
        global last_label
        global number_label
        global balance_label2
        global username_label
        global password_label
        global back_but
        balance_label.grid_forget()
        make_depo_but.grid_forget()
        make_with_but.grid_forget()
        see_details_but.grid_forget()
        logout_but.grid_forget()
        exit_but.grid_forget()
        back_but = Button(root, text='Back', font=('Helvetica', 13), command=lambda: self.back('see_details'))
        first_label = Label(root, text= 'First Name: ' + self.first, font=('Helvetica', 13))
        last_label = Label(root, text='Last Name: ' + self.last, font=('Helvetica', 13))
        number_label = Label(root, text='Account number is: ' + str(self.number), font=('Helvetica', 13))
        balance_label2 = Label(root, text='Balance is: $' + str(self.balance), font=('Helvetica', 13))
        username_label = Label(root, text='Username is: ' + self.username, font=('Helvetica', 13))
        password_label = Label(root, text='Password is: ' + self.password, font=('Helvetica', 13))
        first_label.grid(row=0, column=0)
        last_label.grid(row=1, column=0)
        number_label.grid(row=2, column=0)
        balance_label2.grid(row=3, column=0)
        username_label.grid(row=4, column=0)
        password_label.grid(row=5, column=0)
        back_but.grid(row=6, column=0)

# Creating method that will add to balance
    def deposit(self):
        make_depo_entry_cont = make_depo_entry.get()
        TEMPb = int(self.balance) + int(make_depo_entry_cont)
        TEMPb = str(TEMPb)
        filename2.truncate(0)
        filename2.seek(0)
        filename2.write(TEMPb)

    def back(self, call):
        if call == 'see_details':
            first_label.grid_forget()
            last_label.grid_forget()
            number_label.grid_forget()
            balance_label2.grid_forget()
            username_label.grid_forget()
            password_label.grid_forget()
            back_but.grid_forget()
            where_to.homescreen()

        if call == 'depositwin':
            make_depo_entry.grid_forget()
            make_depo_label.grid_forget()
            make_depo_but1.grid_forget()
            back_but.grid_forget()
            where_to.homescreen()

        if call == 'withwin':
            make_with_entry.grid_forget()
            make_with_but1.grid_forget()
            make_with_label.grid_forget()
            back_but.grid_forget()
            where_to.homescreen()


# Creating method that will withdraw money from balance
    def withdrawl(self):
        make_with_entry_cont = make_with_entry.get()
        TEMPb = int(self.balance) - int(make_with_entry_cont)
        TEMPb = str(TEMPb)
        filename2.truncate(0)
        filename2.seek(0)
        filename2.write(TEMPb)
        

# Creating method that will display deposit window
    def deposit_win(self):
        balance_label.grid_forget()
        make_depo_but.grid_forget()
        make_with_but.grid_forget()
        see_details_but.grid_forget()
        logout_but.grid_forget()
        exit_but.grid_forget()
        global make_depo_entry
        global make_depo_but1
        global back_but
        global make_depo_label
        make_depo_label = Label(root, text="How much do you want to put in?", font=('Helvetica', 13))
        make_depo_but1 = Button(root, text="Make Deposit", font=('Helvetica', 13), command=lambda: self.deposit())
        back_but = Button(root, text='Back', font=('Helvetica', 13), command=lambda: self.back('depositwin'))
        make_depo_entry = Entry(root, width=35, font=('Helvetica', 13))
        make_depo_label.grid(row=0, column=0)
        make_depo_entry.grid(row=1, column=0)
        make_depo_but1.grid(row=2, column=0)
        back_but.grid(row=3, column=0)

# Creating method that will display withdrawl window
    def withdrawl_win(self):
        balance_label.grid_forget()
        make_depo_but.grid_forget()
        make_with_but.grid_forget()
        see_details_but.grid_forget()
        logout_but.grid_forget()
        exit_but.grid_forget()
        global make_with_entry
        global make_with_but1
        global make_with_label
        global back_but
        make_with_label = Label(root, text="How much do you want to take out?", font=('Helvetica', 13))
        make_with_but1 = Button(root, text='Make Withdrawl', font=('Helvetica', 13), command=lambda: self.withdrawl())
        back_but = Button(root, text='Back', font=('Helvetica', 13), command=lambda: self.back('withwin'))
        make_with_entry = Entry(root, width=35, font=('Helvetica', 13))
        make_with_entry.grid(row=1, column=0)
        make_with_but1.grid(row=2, column=0)
        make_with_label.grid(row=0, column=0)
        back_but.grid(row=3, column=0)


# Customer 0 instance of Customer class
ahanj = Customer('Ahan', 'Jaiswal', 0, filename_cont, 'ahanj', '1234')
bobs = Customer('Bob', 'Smith', 1, filename_cont, 'bobs', 'ydispass')
michaelj = Customer('Michael', 'Jackson', 2, filename_cont, 'michaelj', 'random')

# Creating the login function
def login():
    usrnm_entry_cont = usrnm_entry.get()
    pwd_entry_cont = pwd_entry.get()
    usrnm_entry.grid_forget()
    pwd_entry.grid_forget()
    login_but.grid_forget()
    usrnm_label.grid_forget()
    pwd_label.grid_forget()
    exit_but.grid_forget()

    if usrnm_entry_cont == ahanj.username and pwd_entry_cont == ahanj.password:
        ahanj.homescreen()

    elif usrnm_entry_cont == bobs.username and pwd_entry_cont == bobs.password:
        bobs.homescreen()

    elif usrnm_entry_cont == michaelj.username and pwd_entry_cont == michaelj.password:
        michaelj.homescreen() 

    else:
      loginwin()    

def exit_program(mode):

    if mode == 1:
        time.sleep(2)
        sys.exit()
        
    if mode == 2:
        balance_label.grid_forget()
        make_depo_but.grid_forget()
        make_with_but.grid_forget()
        see_details_but.grid_forget()
        exit_but.grid_forget()
        logout_but.grid_forget()
        filename2.close()
        loginwin()   

# Creating login window method
def loginwin():
    global usrnm_entry
    global pwd_entry
    global login_but
    global usrnm_label
    global pwd_label
    global exit_but
    usrnm_entry = Entry(root, width=23, font=('Helvetica', 13))
    pwd_entry = Entry(root, width=23, font=('Helvetica', 13))
    usrnm_label = Label(root, text="Enter Username: ", font=('Helvetica', 13))
    pwd_label = Label(root, text="Enter Password: ", font=('Helvetica', 13))
    login_but = Button(root, text="Login", font=('Helvetica', 13), command=login)
    exit_but = Button(root, text="Exit", font=('Helvetica', 13), command=lambda: exit_program(1))
    usrnm_label.grid(row=0, column=0)
    usrnm_entry.grid(row=0, column=1)
    pwd_label.grid(row=1, column=0)    
    pwd_entry.grid(row=1, column=1)
    login_but.grid(row=3, column=0)
    exit_but.grid(row=3, column=1)

loginwin()

root.mainloop()