a = [[int(x) for x in input().split()] for y in range(6)]
s = -1000000

for i in range(0, 4):
    for j in range(0, 4):
        new_sum = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
        s = max(s, new_sum)
print(s)