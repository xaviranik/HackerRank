s = str(input())

string_list = list(s)
char_list = list()
final_str = str()

for char in string_list:
    if char.islower():
        char_list.append(char.upper())
    else:
        char_list.append(char.lower())

print(final_str.join(char_list))

