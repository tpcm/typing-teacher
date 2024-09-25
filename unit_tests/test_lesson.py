import pytest

from src.lesson import Lesson, Teacher

def test_teacher():
    teacher = Teacher()
    teacher.gen_word()
    assert len(teacher.current_word) == 1

def test_lesson_init():
    teacher = Teacher()
    lesson = Lesson(10, teacher)
    assert lesson.num_rounds == 10
    assert lesson.teacher == teacher
    assert not lesson.lesson_state 

