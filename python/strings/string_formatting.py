n = int(input())
bl = len(bin(n)[2:])
print(bl)
for i in range(1, n+1):
    print("{0:>{l}d} {0:>{l}o} {0:>{l}X} {0:>{l}b}".format(i, l=bl))