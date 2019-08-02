from itertools import product

l1 = list(map(int, input().strip().split()))
l2 = list(map(int, input().strip().split()))

for x in list(product(l1, l2)):
    print(x, end=" ")