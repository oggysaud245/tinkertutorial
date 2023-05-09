'''This program takes a interger input as a miles and converts it 
to kilometers and make use of gui. tkinter as a gui engine'''

import ttkbootstrap as ttk
import tkinter as tk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input*1.61
    output_string.set(km_output)

window = ttk.Window(themename = 'darkly')
window.title('Demo')
# window.geometry('300*150')

#title

title_label = ttk.Label(master=window, text = "Miles to kilometers", font='Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
button = ttk.Button(master = input_frame, text = "Convert" , command = convert)

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output field
output_string = tk.StringVar()
output_label = ttk.Label(master = window, textvariable= output_string, font="Calibri 24 bold")
output_label.pack()
#loop
window.mainloop()