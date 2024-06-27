# Nested Lists
# Developer: Youssef Tarek
# Link: https://www.hackerrank.com/challenges/nested-list/problem


def find_second_lowest(students):
    students_grades = []
    for student in students:
        students_grades.append(student[1])
    sorted_grades = sorted(set(students_grades))
    second_lowest = sorted_grades[1]
    lowest_students = []
    for student in students:
        if student[1] == second_lowest:
            lowest_students.append(student[0])
    for name in sorted(lowest_students):
        print(name)
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    find_second_lowest(students)