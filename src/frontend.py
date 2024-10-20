import tkinter as tk
from tkinter import ttk
from graphics import LessonWindow

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

num_rows = 3
num_cols = 3
margin = 5
screen_x = 800
screen_y = 600
cell_size_x = (screen_x - 2 * margin) / num_cols
cell_size_y = (screen_y - 2 * margin) / num_rows
win = LessonWindow(screen_x, screen_y)
win.welcome()


win.wait_for_close()
print(win._lesson.lesson_state)
