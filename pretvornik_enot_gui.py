# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox

window = Tk()
window.resizable(width=False, height=False)
window.geometry('{}x{}'.format(400, 300))
window.title('Pretvornik enot km/miles')

greeting = Label(window, text="Vpišite število kilometrov v km:", font=(None, 15))
greeting.pack()

km = Entry(window, width=50)
km.pack()

def pretvorba():
    int_km = int(km.get())
    if True:
        miles = 0.621371 * int_km
    tkMessageBox.showinfo("Vrednost v miljah...", miles)

submit = Button(window, text="Izracunaj",width=30, command=pretvorba)
submit.pack()

window.mainloop()


