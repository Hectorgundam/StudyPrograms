
# Importing it and using an alias
import tkinter as tk

root = tk.Tk()

# x value, y value
root.geometry("800x500")

# Setting a title 
root.title("Python's Pizza")

# Area label
label = tk.Label(root, text="Python's Pizza", font=('Arial', 18))
label.pack(padx=20, pady=20)

# Standard text box widget
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

buttonFrame = tk.Frame(root)
# 3 columns
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

# Button is going to be inside of the button frame
btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')

# Another type of layout is place
# anotherbtn = tk.Button(root, text="TEST")
# anotherbtn.place(x=200, y=200, height=100, width=100)

# Not being used for now, just for reference
# Entry (single line) widget
# myEntry = tk.Entry(root)
# myEntry.pack()

# Buttons widget
# button = tk.Button(root, text="Click Me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)








root.mainloop()


# Pythons Pizza

# Description 
# A program where the user can order pizza and customize their toppings 

# Small pizza $15
# Medium pizza $20 
# Large pizza $25

# Add pepperoni on small is $2 and on medium or large is $3
# Add extra cheese any size is $1

# Intro 
# print("Welcome to Python's Pizza! Lets get your order started.")

# # Asking the user what item they would like to order from the menu
# addItem = input("What would you like to order?")




