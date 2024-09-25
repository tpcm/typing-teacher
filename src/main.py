from lesson import Lesson, Teacher

def main():
    teacher = Teacher()
    lesson = Lesson(3, teacher)
    lesson.start_lesson()

if __name__ == "__main__":
    main()