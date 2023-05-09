import tkinter as tk
from tkinter import ttk

def button_func():
    # print(entry.get())
    entry_text = entry.get()
    # update the label 
    # label.config(text = 'some other text')
    # label['text'] = 'some other text'
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())
# window 
window = tk.Tk()
window.title("Getting and setting widgets")

# widgets 
label = ttk.Label(master =window, text="Some text")
label.pack()

entry = ttk.Entry(master =window)
entry.pack()

button = ttk.Button(master =window, text="The button", command=button_func)
button.pack()

#exercises 


def reset():
    entry['state'] = 'enabled'
    label['text'] = 'Some text'

exercise_button = ttk.Button(master =window, text="Enable Button",command= reset)
exercise_button.pack()

# run 
window.mainloop()