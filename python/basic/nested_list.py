N = int(input())

students = list()

for i in range(N):
    students.append([input(), float(input())])

marks = set([students[x][1] for x in range(N)])
marks = list(marks)
marks.sort()

students = [x[0] for x in students if x[1] == marks[1]]
students.sort()

for s in students:
    print(s)
