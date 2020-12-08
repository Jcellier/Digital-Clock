from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()                         # Create our UI for the clock

root.title("Digital clock")         # Set the title of our clock

def clock():
    """
    Function that will set the time of the clock
    :return:
    """
    tick = strftime("%H:%M:%S %p")  # Store the time with the strftime method into the variable "tick"

    label.config(text=tick)         # Config to display the variable tick as text
    label.after(1000, clock)        # Update the display every seconds

label = Label(root, font=("sans", 80), background="yellow", foreground="red")  # Define the font, background and text color

label.pack(anchor="center")         # Center the clock

clock()
mainloop()