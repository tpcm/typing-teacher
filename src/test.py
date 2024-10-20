import tkinter as tk
from tkinter import ttk
from lesson import Lesson, Teacher, Report



num_rows = 3
num_cols = 3
margin = 5
screen_x = 800
screen_y = 600
win = tk.Tk()
win.title("Typing Teacher")
canvas = tk.Canvas(master=win, width=screen_x, height=screen_y)
canvas.pack(fill=tk.BOTH, expand=1)

def start_lesson(self):
    ttk.Button(self._canvas, text="show results", command=self.close).pack()


welcome = "Welcome to the Typing Teacher!"
canvas.create_text(400, 200, text=welcome)
start_button = ttk.Button(canvas, text="start", command=start_lesson)
# start_button.pack()
test_word = "hello"
test_label = tk.Text(canvas)
test_label.pack()
test_label.insert(tk.END,  chars=test_word)
user_input = tk.StringVar()
user_input_entry = ttk.Entry(canvas, width=10, textvariable=user_input)
user_input_entry.pack()

def on_entry(e):
    print(user_input.get())
    user_input_entry.delete(first=0, last=10)

user_input_entry.bind("<Return>", on_entry)

win.mainloop()