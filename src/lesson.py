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
        self.lesson_state = {}

    def play_round(self, round_num: int):
        start_time = time.time()
        test_word, user_input = self.teacher.teach()
        time_taken = time.time() - start_time
        self.lesson_state[round_num] = [test_word, user_input, time_taken]
    
    def start_lesson(self):
        time.sleep(5)
        for num in range(self.num_rounds):
            self.play_round(num)
        print(self.lesson_state)

# TODO evaluate function