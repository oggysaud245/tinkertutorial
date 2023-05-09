from tkinter import ttk
import tkinter as tk

def button_func():
    pass

def exercise_button_func():
    print("hello world!")

# create a window 
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x600")

# ttk label 
label = ttk.Label(master = window, text = "This is text")

label.pack()
# tk label  
text = tk.Text(master = window)
text.pack()

# ttk entry 
entry = ttk.Entry(master = window)
entry.pack()

# excercise label 
exercise_label = ttk.Label(master = window, text = "my Label")
exercise_label.pack()

# ttk button 
button = ttk.Button(master =window, text = "A Button", command = button_func)
button.pack()

# exercise_button = ttk.Button(master = window, text="Exercise Buton", command = exercise_button_func)

exercise_button = ttk.Button(master = window, text="Exercise Buton", command = lambda:print("Hello"))
exercise_button.pack()


# run 

window.mainloop()
