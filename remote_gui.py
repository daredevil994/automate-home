#import tkinter library
from tkinter import *
#import functions for ON/OFF Variables from functions.py
import functions

#make GUI
main=Tk()
main.title("Home Control")
main.geometry("180x500")

#adding a frame
GUIFrame=Frame(main)
GUIFrame.grid(row =1,column=0,sticky=W)

#adding labels
Label(main,text="Power Buttons",fg='white',bg='black').grid(row=0,column=0,sticky=W)

#add buttons
#add buttons
Button(GUIFrame, text="Light On", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button1.tx).grid(row=2, column=0, sticky=W)
Button(GUIFrame, text="Light Off", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button2.tx).grid(row=2, column=1, sticky=E)
Button(GUIFrame, text="Fan On", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button3.tx).grid(row=3, column=0, sticky=W)
Button(GUIFrame, text="Fan Off", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button4.tx).grid(row=3, column=1, sticky=E)
Button(GUIFrame, text="TV On", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button5.tx).grid(row=4, column=0, sticky=W)
Button(GUIFrame, text="TV Off", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button6.tx).grid(row=4, column=1, sticky=E)
Button(GUIFrame, text="AC On", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button7.tx).grid(row=5, column=0, sticky=W)
Button(GUIFrame, text="AC Off", width=8, height=4,bg='light blue',font=16,border=6,fg='black', command=functions.button8.tx).grid(row=5, column=1, sticky=E)
Button(GUIFrame, text="All On", width=8, height=4,bg='light green',font=16,border=6,fg='black', command=functions.button9.tx).grid(row=6, column=0, sticky=W)
Button(GUIFrame, text="All Off", width=8, height=4,bg='light green',font=16,border=6,fg='black', command=functions.button10.tx).grid(row=6, column=1, sticky=E)

#button init
main.mainloop()