import random
from tkinter import *

root = Tk()
root.geometry("600x300")

text1 = Label(root,text='',font = ("arial",300))
def roll_dice():
    # We use the ascii code for dice numbers.
    num_code = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    text1.config(text=f'{random.choice(num_code)}{random.choice(num_code)}')
    text1.pack()
    

button1 = Button(root,text="Roll the dice", command = roll_dice)
button1.place(x=250,y=0)

root.mainloop()
