n = int(input())
def foo(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)
    list1 = [*reversed(b)]
    for i in range(len(list1)):
        list1[i] = int(list1[i])
        list1[i] = list1[i] * (2 ** i)
    res = sum(list1)
    print(res)


foo(n)
