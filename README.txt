This is the Banking program V4 by Ahan Jaiswal, it is not intended for personal or commercial use

The default logins are:

username: ahanj
password: 1234

username: bobs
password: ydispass

username: michaelj
password: random



This program uses Object Oriented Programming, or more commonly known as OOP, this program also uses tkinter, a module used for creating GUI's as well as other GUI related
apparatus'. Because of the way I designed the code, adding a new user is quite simple, though a option to add one from a GUI is coming in the future. Here are the following 
steps:

 - First, you have to add your user instance, the name of your instance should be your initials, like Bob Smith would be bobs, the variables would be your first name, your 
last name, your account number, your balance, (type in filename_cont for balance), your username (type in your instance name for this one), and your password. For example:

 michaelj = ('Michael', 'Jordan', 1, filename_cont, 'michaelj', 'random')


 - Next, you have to change 2 conditional loops, one for logging in (reckognizing your username and password), and one for opening a file (checks your username, and opens the 
relative file)

in the login function, you need to add the lines:

if usrnm_entry_cont == yourusername.username and pwd_entry_cont == yourusername.password:
        yourusername.homescreen()

in the open_files method you need to add the lines:
if where_to == yourusername.username:
            where_to = yourusername ( <-- do not add quotes to yourusername here)

 - Last, you just need to create a txt file for your account, name it your instance name. For example: michaelj, and type in 0, 
 (so the program can read it)

 yourusername.txt, inside this file, just type 0, and do not modify it

This might be confusing at first, but you will get used to it as it's a easy thing to remember

Like I mentioned earlier, I use tkinter, and Object Oriented Programming as my main components of the program, as well as those 2 main things, I use some basics of python:

 - Conditional Statements
 - Functions
 - User input (through tkinter)
 - Text Files
 - Module importing

 