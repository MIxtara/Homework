list1 = [1, 2, 3, 4, 5]
n = int(input('Указаное число:'))
for i in range(len(list1)):
    list1[i] += n
print(list1)
