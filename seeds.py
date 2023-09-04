from datetime import datetime
from random import randint

from faker import Faker

from database.db import session
from database.models import Group, Student, Teacher, Subject, Grade

fake_data = Faker("uk_UA")


NUMBER_STUDENTS = 40
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 3
NUMBER_GRADES = 400


def create_groups():
    for i in range(NUMBER_GROUPS):
        group = Group(
            groupname = i+1 
        )
        session.add(group)
    session.commit()


def create_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
        first_name = fake_data.first_name(),
        last_name = fake_data.last_name(),
        group_id = randint(1, NUMBER_GROUPS)
            )
        session.add(student)
    session.commit()


def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            first_name = fake_data.first_name(),
            last_name = fake_data.last_name()
            )
        session.add(teacher)
    session.commit()


def create_subjects():
    for i in ["JavaScript", "Java", "Python", "C#",
                         "TypeScript", "PHP", "Kotlin", "C++"]:
        subject = Subject(
            subject_name = i,
            teacher_id = randint(1, NUMBER_TEACHERS)
        )
        session.add(subject)
    session.commit()


def create_grades():
    for _ in range(NUMBER_GRADES):
        grade = Grade(
            grade = randint(1, 12),
            grade_date = fake_data.date_between_dates(date_start=datetime(2022, 9, 1), date_end=datetime(2023, 5, 31)),
            student_id = randint(1, NUMBER_STUDENTS),
            subject_id = randint(1, NUMBER_SUBJECTS)
        )
        session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_groups()
    create_students()
    create_teachers()
    create_subjects()
    create_grades()

