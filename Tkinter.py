from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!").grid(row = 1, column = 0)
myLabel2 = Label(root, text = "Bullshit").grid(row = 1, column = 2)


root.mainloop()