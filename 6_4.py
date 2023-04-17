list1 = [3, 2, 4, 'фаыфа', 'эцуацуа', True, False]
i = 0
while True:
    if not isinstance(list1[i], str):
        del(list1[i])
    else:
        i += 1
print(list1)
