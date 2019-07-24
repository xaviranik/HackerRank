n = int(input())
l = list(map(int, input().split()))

rl = l[::-1]

print(' '.join(str(e) for e in rl))