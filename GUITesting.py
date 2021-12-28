"""Followed along from TheCodex's youtube tutorial on Tkinter."""
from tkinter import *
import tkinter as tk
import time

num_clicks = 0

def buttonListener() -> None:
    global num_clicks
    num_clicks += 1
    print('hello world')
    print('click #' + str(num_clicks))

root = Tk()

# size of the window (pixels) 
root.geometry('300x300')

# variable common to a certain number of buttons
v = tk.IntVar()

# parameters: container, text
l = Label(root, text='hello world')

# parameters: container, text, listener function (no brackets)
b = Button(root, text='click me daddy', command=buttonListener)

# creating a menubutton, adding menu to button, associating menu with menubutton
mb = Menubutton(root, text='my menu')
mb.menu = Menu(mb)
mb['menu'] = mb.menu

# creating a radiobutton
radioButton1 = Radiobutton(root, text='it is sunny', variable=v, value=0, command=lambda: print(v.get()))
radioButton2 = Radiobutton(root, text='it is rainy', variable=v, value=1, command=lambda: print(v.get()))

# adding a command with a label and an associated function
# (a lambda is just a shortcut for making a simple function)
mb.menu.add_command(label='option 1', command=lambda: print('this is option 1'))
mb.menu.add_command(label='option 2', command=lambda: print('this is option 2'))

# creating a canvas
c = Canvas(root, height=150, width=150, background='grey')

# creating a line inherent to canvas c (does not need to be packed)
# 'width' means thickness
line1 = c.create_line(5, 5, 125, 75, width=5)

# creating an oval
oval1 = c.create_oval(20, 20, 100, 100, fill='red')

# creating an oval animation function
def move_oval() -> None:
    global c
    coords = [20, 20, 100, 100]
    root.update()
    time.sleep(0.1)
    for i in range(1, 50):
        c.create_oval(coords[0], coords[1], coords[2], coords[3], fill = 'grey')
        for j in range(0, 3):
            coords[j] = coords[j] + 1
        c.create_oval(coords[0], coords[1], coords[2], coords[3], fill = 'red')

move_button = Button(root, text='move circle', command=move_oval)


# packs element into the assigned root container. parameters: position on side
l.pack()
b.pack(side=BOTTOM)
mb.pack()
radioButton1.pack(side=LEFT)
radioButton2.pack(side=LEFT)
c.pack()
move_button.pack(side=BOTTOM)


root.mainloop()