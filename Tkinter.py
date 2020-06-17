from tkinter import *

root = Tk()

def myClick():
    myLable = Label(root, text=e.get())
    myLable.pack()

e = Entry(root, width = 100)
e.get()
e.pack()
e.insert(0, "Blabla: ")


myButton = Button(root, text ="Click me!", pady=50, padx = 100, command=myClick, fg="red")
myButton.pack()

root.mainloop()