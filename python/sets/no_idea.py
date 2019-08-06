n = (input().split())
l = map(int, input().strip().split())
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

res = 0
for i in l:
    if i in A:
        res += 1
    if i in B:
        res -= 1
print(res)