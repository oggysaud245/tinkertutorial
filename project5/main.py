import tkinter as tk
from tkinter import ttk

#  buttons in tkinter 

window = tk.Tk()
window.title("Button")
window.geometry("600x400")

# # button 
# def button_func():
#     print("Button clicked")

# button_string = tk.StringVar(value="A Button with string var")

# button = ttk.Button(window, text="A simple button",command=button_func, textvariable=button_string)
# button.pack()

# #  check button 
# check_var = tk.IntVar(value=10) # tk.StringVar() #IntVar()  #BooleanVar()
# check1 = ttk.Checkbutton(window,
#                         text="Check Box 1",
#                         command=lambda:print(check_var.get()),
#                         variable=check_var,
#                         onvalue=10,
#                         offvalue = 5)
# check1.pack()

# check2 = ttk.Checkbutton(window,
#                         text="Check Box 2",
#                         command=lambda:check_var.set(5))
# check2.pack()

# # radio buttons 
# radio_var = tk.StringVar()
# radio1 = ttk.Radiobutton(window,
#                         text="Radio Button 1",
#                         value=1,
#                         variable=radio_var,
#                         command=lambda:print(radio_var.get()),)
# radio2 = ttk.Radiobutton(window,
#                         text="Radio Button 2",
#                         variable=radio_var,
#                         value = 2,
#                         command=lambda:print(radio_var.get()))
# radio1.pack()
# radio2.pack()

# exercise 
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = tk.StringVar()
check_bool = tk.BooleanVar()
radiobutton1 = ttk.Radiobutton(window, text="Radio A", value="A", command = radio_func, variable=radio_string)

radiobutton2 = ttk.Radiobutton(window, text="Radio B", value="B", command= radio_func, variable=radio_string)

radiobutton1.pack()

radiobutton2.pack()

check1 = ttk.Checkbutton(window, text="Check",
                        variable=check_bool,
                        command= lambda x:print(radio_string.get()))
check1.pack()

# run 
window.mainloop()