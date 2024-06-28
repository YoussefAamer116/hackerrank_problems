# Finding The Percentage Problem
# Developer: Youssef Tarek
# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':

    def find_percentage(student_marks):
        for key, value in student_marks.items():
            if key == query_name:
                num = 0
                total = 0
                for x in value:
                    num += 1
                    total += x
        print(f"{round(total/num, 2):.2f}")

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    find_percentage(student_marks)
