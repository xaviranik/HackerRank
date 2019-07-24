n = int(input())
d = {}

for i in range(0, n):
    key, value = input().split()
    d[key] = int(value)

for i in range(0, n):
    search = str(input())
    res = d.get(search, 'none')
    if res != 'none':
        print('{}={}'.format(search, d[search]))
    else:
        print('Not found')