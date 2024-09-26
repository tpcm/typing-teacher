import random
import string
import time

class Teacher:
    def __init__(self):
        self.current_word: str

    def gen_word(self):
        self.current_word = random.choice(string.ascii_lowercase)

    def teach(self):
        self.gen_word()
        print(self.current_word)
        user_input = input()
        return self.current_word, user_input
        
        
class Lesson:
    def __init__(self, num_rounds: int, teacher: Teacher):
        self.num_rounds = num_rounds
        self.teacher = teacher
        self.lesson_state: dict[list[str | float]] = {}

    def play_round(self, round_num: int):
        start_time = time.time()
        test_word, user_input = self.teacher.teach()
        time_taken = time.time() - start_time
        self.lesson_state[round_num] = [test_word, user_input, time_taken]
    
    def start_lesson(self):
        # time.sleep(5)
        for num in range(self.num_rounds):
            self.play_round(num)
        print(self.lesson_state)

# TODO evaluate function
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