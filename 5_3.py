n = int(input())
c = 0
for i in range(2, n+1, 2):
    print(i, end=' ')
    c += 1
    if not c % 5:
        c = 0
        print()