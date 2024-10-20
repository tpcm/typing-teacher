import tkinter as tk
from tkinter import ttk
from lesson import Lesson, Teacher, Report


class Window:
    def __init__(self, width, height):
        self._root = tk.Tk()
        self._root.title("Typing Teacher")
        self._canvas = tk.Canvas(master=self._root, width=width, height=height)
        self._canvas.pack(fill=tk.BOTH, expand=1)
        self.window_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False


class LessonWindow(Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self._teacher = Teacher()
        self._lesson = Lesson(self._teacher, self._canvas)

    def welcome(self):
        welcome = "Welcome to the Typing Teacher!"
        welcome_label = tk.Label(self._canvas, text=welcome)
        welcome_label.place(x=290, y=200)

        rounds_msg = "Please select the number of rounds you wish to complete."
        rounds_label = tk.Label(self._canvas, text=rounds_msg)
        rounds_label.place(x=210, y=300)
        user_input = tk.StringVar()
        user_input_entry = ttk.Entry(
            self._canvas, width=5, textvariable=user_input)
        user_input_entry.focus_set()
        user_input_entry.place(x=370, y=330)

        def on_entry(e):
            print(user_input.get())
            self._lesson.set_num_rounds(user_input.get())
            user_input_entry.destroy()
            welcome_label.destroy()
            rounds_label.destroy()
            self.show_start_button()
            user_input_entry.unbind("<Return>")

        user_input_entry.bind("<Return>", on_entry)

    def show_start_button(self):
        rounds_msg = (
            "Press the start button to begin your lesson!\n"
            "(The curser will automatically focus on the text entry box)"
        )
        rounds_label = tk.Label(self._canvas, text=rounds_msg)
        rounds_label.place(x=200, y=300)
        self.start_button = ttk.Button(
            self._canvas, text="start", command=self._lesson.start_lesson)
        self.start_button.focus_set()
        def on_entry(e):
            self._lesson.start_lesson()
        self.start_button.bind("<Return>", on_entry)
        self.start_button.place(x=350, y=400)
