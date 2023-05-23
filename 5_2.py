num1 = int(input('1-ое число '))
sin = input('Введите знак ')
num2 = int(input('2-ое число '))
if sin == '+':
    print(num1 + num2)
elif sin == '-':
    print(num1 - num2)
elif sin == '*':
    print(num1 * num2)
else:
    print(num1 / num2)

