from tkinter import * # Import tkinter

# Make tkinter window
root = Tk() # Define the window
root.title("Simple window") # Change window title
root.geometry("800x410") # Change window size
root.resizable(False, False) # Lock window size

# Functions
def clicked(): # Function that changes the text of label
    label1.config(text="Clicked!") # Change label text
    root.after(2000, reset) # Reset label text after 2000 ms

def reset(): # Function that reset label
    label1.config(text="Not clicked") # Change label text

# Widgets
button1 = Button(root, text="Click me!", fg="white", bg="black", font=("Arial", 20), command=clicked) # Define the button
button1.place(x=300, y=150) # Place the button

label1 = Label(root, text="Not clicked", font=("Arial", 60)) # Define the label
label1.pack() # Place the label

root.mainloop() # Window loop
