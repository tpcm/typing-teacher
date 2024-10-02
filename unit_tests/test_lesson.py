import pytest

from src.lesson import Lesson, Teacher, Report

def test_teacher_gen_char():
    teacher = Teacher()
    teacher.gen_char()
    assert len(teacher.current_char) == 1

def test_teacher_gen_word():
    teacher = Teacher()
    teacher.gen_random_word()
    assert len(teacher.current_word) >= 4
    assert  len(teacher.current_word) <= 6

def test_lesson_init():
    teacher = Teacher()
    lesson = Lesson(10, teacher)
    assert lesson.num_rounds == 10
    assert lesson.teacher == teacher
    assert not lesson.lesson_state 

def test_report_eval_each_round_succeed():
    lesson_state = {0: ['s', 's', 1.0], 1: ['u', 'u', 1.0], 2: ['q', 'q', 1.0]}
    report = Report(lesson_state)
    report.eval_each_round()
    assert report.per_round_report[0][0] == True
    assert report.per_round_report[1][0] == True
    assert report.per_round_report[2][0] == True
    assert report.per_round_report[0][1] == 1.0
    assert report.per_round_report[1][1] == 1.0
    assert report.per_round_report[2][1] == 1.0

def test_report_eval_final_score():
    lesson_state = {0: ['s', 's', 1.0], 1: ['u', 'u', 1.0], 2: ['q', 'q', 1.0]}
    report = Report(lesson_state)
    report.eval_each_round()
    report.eval_final_score()
    assert report.all_rounds_evaluation[0] == 1.0
    assert report.all_rounds_evaluation[1] == 3.0
    assert report.all_rounds_evaluation[2] == 1.0