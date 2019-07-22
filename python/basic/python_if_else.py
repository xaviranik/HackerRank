
i = int(input().strip())

if 1 <= i <= 100:
    if not i % 2 == 0:
        print("Weird")
    else:
        if 2 <= i <= 5:
            print("Not Weird")
        elif 6 <= i <= 20:
            print("Weird")
        elif i > 20:
            print("Not Weird")
