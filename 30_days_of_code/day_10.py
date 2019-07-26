n = int(input())
li = list(format(n, 'b'))

counter = 0
result = 0

for n in li:
    if n == '1':
        counter += 1
        result = max(counter, result)
    else:
        counter = 0

print(result)