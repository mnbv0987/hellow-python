

#Program to demonstrate GUI programming in Python.
import tkinter
top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()


import tkinter
from tkinter import message
top = tkinter.Tk()
def helloCallBack():
    message.showinfo( "Hello Python", "Hello World")
B = tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()


from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()


from tkinter import *
from tkinter import message
master = Tk()
master.geometry('500x200')
def func():
    message.showinfo( "Hello Educba", "Press any key on the keyboard")
b1 = Button( master, text='Click me for next step', background= 'Cyan', fg = '#000000', command = func)
b1.pack()
def Keyboardpress( key):
    key_char = key.char
    print( key_char, 'key button is pressed on the keyboard')
master.bind( '', lambda i : Keyboardpress(i))
master.mainloop()
