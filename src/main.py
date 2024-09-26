from lesson import Lesson, Teacher, Report

def main():
    teacher = Teacher()
    lesson = Lesson(3, teacher)
    lesson.start_lesson()
    report = Report(lesson.lesson_state)
    report.eval_each_round()
    report.eval_final_score()
    print(report.per_round_report)
    print(report.all_rounds_evaluation)


if __name__ == "__main__":
    main()