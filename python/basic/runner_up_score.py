n = int(input().strip())

champ = -1000
runner_up = -1000

if 2 <= n <= 10:
    A = [int(i) for i in input().split()]

    for i in A:
        if -100 <= i <= 100:
            if i > champ:
                runner_up = champ
                champ = i
            elif runner_up < i < champ:
                runner_up = i
    print(runner_up)
