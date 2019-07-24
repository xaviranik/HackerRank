n, m = list(map(int, input().split()))
cm = 1
mid = int(n/2) + 1

for i in range(1, n+1):
    if i == mid:
        x = int((m - 7)/2)
        print('-' * x + 'WELCOME' + '-' * x)
    elif i < mid:
        x = int((m - 3 * cm)/2)
        print('-' * x + '.|.' * cm + '-' * x)
        cm += 2
    elif i > mid:
        cm -= 2
        x = int((m - 3 * cm)/2)
        print('-' * x + '.|.' * cm + '-' * x)