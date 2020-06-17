from tkinter import *

root = Tk()

def myClick():
    myLable = Label(root, text="Clicked")
    myLable.pack()

myButton = Button(root, text ="Click me!", pady=50, padx = 100, command=myClick, fg="red")
myButton.pack()

root.mainloop()