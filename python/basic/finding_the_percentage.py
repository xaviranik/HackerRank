n = int(input().strip())
std_map = {}
total = 0

for i in range(n):
    std_list = [str(inp) for inp in input().split()]
    std_map[std_list[0]] = std_list[1:]

name = str(input().strip())

if name in std_map:
    marks = list(map(float, std_map.get(name)))
    for mark in marks:
        total += mark

    print("%.2f" % (total/len(marks)))

