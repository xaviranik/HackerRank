string = input()
l = list(string)
l[0] = l[0].capitalize()

for i in range(0, len(l) - 1):
    if l[i] == ' ':
        l[i+1] = l[i+1].capitalize()
print(''.join(l))