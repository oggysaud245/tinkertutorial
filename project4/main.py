import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Tkinter Variables")

# tkinter variables
string_var = tk.StringVar(value="Start value")

# widgets 
label = ttk.Label(master = window, text = "some text", textvariable= string_var)
label.pack()

# entry
entry = ttk.Entry(master = window, textvariable= string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable= string_var)
entry2.pack()

def func():
    print(string_var.get())

button = ttk.Button(master = window,text = "button", command = func)
button.pack()

# exercise 
exercise_var = tk.StringVar(value="test")

exercise_label = ttk.Label(master = window, text = "exercise", textvariable= exercise_var)

exercise_label.pack()

entry3 = ttk.Entry(master = window, textvariable= exercise_var)
entry4 = ttk.Entry(master = window, textvariable= exercise_var)
entry3.pack()
entry4.pack()
#run
window.mainloop()
