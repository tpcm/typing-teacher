import random
import string
import time
import tkinter as tk
from tkinter import ttk

class Teacher:
    def __init__(self):
        self.current_char: str
        self.current_word: str

    def gen_char(self):
        self.current_char = random.choice(string.ascii_lowercase)

    def reset_current_word(self):
        self.current_word = ""

    def gen_random_word(self):
        self.reset_current_word()
        word_length = random.randint(4, 6)
        for _ in range(word_length):
            self.gen_char()
            self.current_word = "".join([self.current_word, self.current_char])

    def teach(self):
        self.gen_random_word()
        return self.current_word


class Lesson:
    def __init__(self, teacher: Teacher, canvas: tk.Canvas):
        self.teacher = teacher
        self.canvas = canvas
        self.lesson_state: dict[list[str | float]] = {}
        self.current_test_word: str
        self.test_label = tk.Label(self.canvas)
        self.current_round = 0
        self.round_start_time: float
        self.num_rounds: int

    def set_num_rounds(self, num_rounds):
        self.num_rounds = int(num_rounds)
    
    def show_test_word(self):
        self.current_test_word = self.teacher.teach()
        self.test_label["text"] = self.current_test_word
        self.test_label.place(x=375, y=200)

    def play_round(self):
        print(self.num_rounds)
        self.show_test_word()
        user_input = tk.StringVar()
        user_input_entry = ttk.Entry(self.canvas, width=10, textvariable=user_input)
        user_input_entry.focus_set()
        user_input_entry.place(x=350, y=400)
        self.round_start_time = time.time()

        def on_entry(_):
            self.current_round += 1
            self.lesson_state[self.current_round] = [
                self.current_test_word, user_input.get(), time.time() - self.round_start_time
            ]
            print(f"Current round: {self.current_round}, Number of rounds: {self.num_rounds}")
            print(f"Type of current_round: {type(self.current_round)}, Type of num_rounds: {type(self.num_rounds)}")
            if self.current_round == self.num_rounds:
                print("Ending lesson")
                self.wipe_canvas()
                self.end_lesson()
            
            user_input_entry.delete(first=0, last=10)
            self.show_test_word()
            self.round_start_time = time.time()

        user_input_entry.bind("<Return>", on_entry)

    def check_end_lesson(self):
        if self.current_round == self.num_rounds:
            print("yayay")
            self.wipe_canvas()
            self.end_lesson()
            

    def end_lesson(self):
        self.wipe_canvas()
        end_msg = "The lesson has finished, your results are shown below, thank you!"
        end_label = tk.Label(self.canvas, text=end_msg)
        end_label.place(x=210, y=300)
        self.show_results()
    
    def show_results(self):
        report = Report(self.lesson_state)
        report.eval_each_round()
        report.eval_final_score()
        total_score, total_time_taken, time_per_round = report.all_rounds_evaluation
        final_score_msg = (
            f"total_score: {round(total_score, 2)}\n "
            f"total_time_taken: {round(total_time_taken, 2)} seconds "
            f"time_per_round: {round(time_per_round, 2)} seconds"
        )
        final_score_label = tk.Label(self.canvas, text=final_score_msg)
        final_score_label.place(x=200, y=400)

    def start_lesson(self):
        self.wipe_canvas()
        self.play_round()

    def wipe_canvas(self):
        for slave in self.canvas.place_slaves():
            slave.destroy()



class Report:
    def __init__(self, lesson_state: dict[list[str | float]]) -> None:
        self.lesson_state = lesson_state
        self.per_round_report: dict[list[bool | float]]
        self.all_rounds_evaluation: tuple[float]
        self.lesson_report = self.produce_report()

    def produce_report(self):
        pass
    
    def eval_each_round(self):
        per_round_report = {}
        for key, value in self.lesson_state.items():
            ground_truth = value[0]
            user_answer = value[1]
            correct = True if ground_truth == user_answer else False
            per_round_report[key] = [correct, value[-1]]
        self.per_round_report = per_round_report
    
    def eval_final_score(self):
        total_correct = []
        total_time = 0
        for value in self.per_round_report.values():
            total_correct.append(value[0])
            total_time += value[1]
        total_correct = sum(filter(lambda x: True, total_correct))
        self.all_rounds_evaluation = (
            total_correct/len(self.lesson_state),
            total_time,
            total_time/len(self.lesson_state)
            )