from tkinter import *
from tkinter import ttk
import random

# Initialising width of the screen 
WIDTH = 500
# Initialising height of the screen 
HEIGHT = 500
# Initialising speed of the snake 
SPEED = 200
# Initialising space of the screen 
SPACE_SIZE = 20
# Initialising body's length of the snake 
BODY_SIZE = 2
# Initialising color of the snake 
SNAKE = "#00FF00"
# Initialising colour of the food 
FOOD = "#FFFFFF"
# Initialising colour of the background 
BACKGROUND = "#000000"



window = Tk() 
window.title("SNAKE") 
frame = ttk.Frame(window, padding=10)
ttk.Label(frame, text="SNAKE").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1,row=0)





w = Canvas(window, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height/2)
w.create_line(0,y,canvas_width, y)









window.mainloop()