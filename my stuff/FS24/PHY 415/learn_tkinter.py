#learn tkinter

import tkinter as tk
from tkinter import ttk

#first_label = tk.StringVar()

def new_text(widget, new_name):
    widget['text'] = new_name

def lets_do_it():
    new_text(the_only_button, 'well done')
    

window = tk.Tk()
window.title('Learn tkinter')

the_only_button = ttk.Button(master=window, text='nice cock', command=lets_do_it)
the_only_button.pack()

rename_text = ttk.Entry(master=window)
rename_text.pack

window.mainloop()
