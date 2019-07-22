t = int(input())
for i in range(t):
    e_list = list()
    o_list = list()
    string = input()
    for x in range(0, len(string)):
        if x % 2 == 0:
            e_list.append(string[x])
        else:
            o_list.append(string[x])
    print('{} {}'.format(''.join(e_list), ''.join(o_list)))