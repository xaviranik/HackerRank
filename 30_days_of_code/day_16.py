i = input().strip()

try:
    print(int(i))
except ValueError as error:
    print('Bad String')