import Tkinter
from Tkinter import *
import tkMessageBox
from subprocess import call
import pandas as pd

top = Tkinter.Tk()
top.resizable(width=False, height=False)
top.minsize(width=300, height=300)
top.title("SIS Google Sync")

#def SIS():

#def GOOGLE():

def compmerge():
    a = pd.read_csv("testid.csv")
    b = pd.read_csv("test.csv")
    b = b.dropna(axis=1)
    merged = a.merge(b, on='Serial Number')
    merged.to_csv("output.csv", index=False)


B1 = Tkinter.Button(top, text ="Pull From SIS", width =20)
B2 = Tkinter.Button(top, text ="Pull From Google", width = 20)
B3 = Tkinter.Button(top, text ="Sync CSV", width = 20, command = compmerge)


B1.pack()
B2.pack()
B3.pack()
top.mainloop()