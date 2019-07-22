str = input()

if any(x.isalnum() for x in str):
    print('True')
else:
    print('False')

if any(x.isalpha() for x in str):
    print('True')
else:
    print('False')

if any(x.isdigit() for x in str):
    print('True')
else:
    print('False')

if any(x.islower() for x in str):
    print('True')
else:
    print('False')

if any(x.isupper() for x in str):
    print('True')
else:
    print('False')

# Another interesting solution
# inp = input()
# print(any(x.isalnum() for x in inp))
# print(any(x.isalpha() for x in inp))
# print(any(x.isdigit() for x in inp))
# print(any(x.islower() for x in inp))
# print(any(x.isupper() for x in inp))