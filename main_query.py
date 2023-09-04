from sqlalchemy import func, desc, and_

from database.db import session
from database.models import Group, Student, Teacher, Subject, Grade


def get_query_1():
    result = (
        session.query(
            Student.last_name, func.round(func.avg(Grade.grade), 2).label("avg_rate")
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg_rate"))
        .limit(5)
        .all()
    )
    # print(result)
    print(f"This students has highest average grade")
    for i in result:
        print(f"Student {i[0]} has average grade {i[1]}")


def get_query_2():
    subject_id = 1 # 2 # 3
    result = (
        session.query(
            Student.last_name,
            func.round(func.avg(Grade.grade), 2).label("avg_rate"),
            Subject.subject_name,
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .filter(Subject.id == subject_id)
        .group_by(Subject.id, Student.id)
        .order_by(desc("avg_rate"))
        .first()
    )
    # print(result)
    result_list = []
    for i in result:
        result_list.append(str(i))
    print(f"Student {result_list[0]} has higest average grade {result_list[1]} by selected subject {result_list[2]}")


def get_query_3():
    subject_id = 3
    group_id = 2
    result = (
        session.query(
            Subject.subject_name,
            Group.groupname,
            func.round(func.avg(Grade.grade), 2).label("avg_rate"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Subject.id == subject_id, Group.id == group_id)
        .group_by(Group.id, Subject.id)
        .order_by(desc("avg_rate"))
        .first()
    )
    # print(result)
    res = list()
    for i in result:
        res.append(i)
    print(f'Subject: {res[0]}, Group: {res[1]}, average grade: {res[2]}')


def get_query_4():
    result = (
        session.query(
        func.round(func.avg(Grade.grade), 2))
        .select_from(Grade)
        .one()
    )
    # print(result)
    for i in result:
        print(f'Average grade: {str(i)}')


def get_query_5():
    teacher_id = 1 #2 #3
    result = (
        session.query(Teacher.last_name, Subject.subject_name)
        .select_from(Subject)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .all()
    )
    # print(result)
    teacher_list = list()
    subject_list = list()
    for i in result:
        teacher_list.append(i[0])
        subject_list.append(i[1])

    print(f"Teacher: {teacher_list[0]}, teach subjects: {subject_list}")


def get_query_6():
    group_id = 1 #2 #3
    result = (
        session.query(Group.id, Student.last_name)
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .order_by(Group.id, Student.last_name)
        .all()
    )

    # print(result)
    print(f'Students in selected group: ')
    for i in result:
        print(f"Group: {i[0]}, Student: {i[1]}")


def get_query_7():
    group_id = 1 #2 #3
    subject_id = 3 #2 #1 #4 #5 #6 #7 #8
    result = (
        session.query(Group.id, Subject.subject_name, Student.last_name, Grade.grade)
        .select_from(Grade)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(Group.id == group_id, Subject.id == subject_id)
        .order_by(Student.last_name)
        .all()
    )
    print(f'Students grades by selected group and subject: ')
    for i in result:
        print(f"Group: {i[0]}, Subject: {i[1]}, Student: {i[2]}, Grade: {i[3]}")


def get_query_8():
    teacher_id = 2 #1 #3
    result = (
        session.query(Teacher.last_name, func.round(func.avg(Grade.grade), 2))
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .group_by(Teacher.id)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    # print(result)
    for i in result:
        print(f"Teacher: {i[0]}, average grade by it's subject: {i[1]}")


def get_query_9():
    student_id = 10 # 1...40
    result = (
        session.query(Student.last_name, Subject.subject_name)
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .group_by(Student.last_name, Subject.subject_name)
        .filter(Student.id == student_id)
        .all()
    )
    # print(result)
    student_list = list()
    subject_list = list()
    for i in result:
        student_list.append(i[0])
        subject_list.append(i[1])

    print(f"Student: {student_list[0]} study subjects: {subject_list}")


def get_query_10():
    student_id = 10 # 1...40
    teacher_id = 2 #1 #3
    result = (
        session.query(Subject.subject_name, Student.last_name, Teacher.last_name)
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Teacher)
        .group_by(Subject.subject_name, Student.last_name, Teacher.last_name)
        .filter(Student.id == student_id, Teacher.id == teacher_id)
        .all()
    )
    # print(result)
    subject_list = list()
    student_list = list()
    teacher_list = list()
    for i in result:
        subject_list.append(i[0])
        student_list.append(i[1])
        teacher_list.append(i[2])
    print(f'Subjects {subject_list} for student {student_list[0]} teaches by teacher {teacher_list[0]}')


if __name__ == "__main__":
    print("QUERY 01")
    get_query_1()
    print("*" * 100)
    print("QUERY 02")
    get_query_2()
    print("*" * 100)
    print("QUERY 03")
    get_query_3()
    print("*" * 100)
    print("QUERY 04")
    get_query_4()
    print("*" * 100)
    print("QUERY 05")
    get_query_5()
    print("*" * 100)
    print("QUERY 06")
    get_query_6()
    print("*" * 100)
    print("QUERY 07")
    get_query_7()
    print("*" * 100)
    print("QUERY 08")
    get_query_8()
    print("*" * 100)
    print("QUERY 09")
    get_query_9()
    print("*" * 100)
    print("QUERY 10")
    get_query_10()
    print("*" *100)