n = int(input())
a = input()
t = tuple(int(x) for x in a.split())
print(hash(t))