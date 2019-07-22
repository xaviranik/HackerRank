
L = []

no_of_inp = int(input())

for i in range(no_of_inp):
    inputs = input()
    lst_of_input = [i for i in inputs.split()]
    if lst_of_input[0] == 'insert':
        L.insert(int(lst_of_input[1]), int(lst_of_input[2]))
    elif lst_of_input[0] == 'print':
        print (L)
    elif lst_of_input[0] == 'remove':
        L.remove(int(lst_of_input[1]))
    elif lst_of_input[0] == 'append':
        L.append(int(lst_of_input[1]))
    elif lst_of_input[0] == 'sort':
        L.sort()
    elif lst_of_input[0] == 'pop':
        L.pop()
    elif lst_of_input[0] == 'reverse':
        L.reverse()