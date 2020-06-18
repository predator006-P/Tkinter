from tkinter import *

root = Tk()
root.title('ZF message catalog')
root.iconbitmap('C:/Users/pnemeth/Downloads/zf_official_logo_svg_TVG_icon.ico')
def myClick():
    myLable = Label(root, text=e.get())
    myLable.pack()

e = Entry(root, width = 100)
e.get()
e.pack()
e.insert(0, "Blabla: ")

myButton = Button(root, text ="Click me!", pady=50, padx = 100, command=myClick, fg="red")
button_quit = Button(root, text = "Close", command = root.quit)
button_quit.pack()
myButton.pack()

root.mainloop()