i = int(input())

for i in range(i):
    tmp = str(input()).split()
    f = int(tmp[0])
    s = int(tmp[1])

    maximum = 0

    for j in range(1, f):
        for k in range(j + 1, f + 1):
            h = j & k
            if s > h > maximum:
                maximum = h

    print(maximum)