name = input('Введите ваше имя: ')
age = int(input('Введите ваш возраст: '))
city = input('Введите город, в котором проживаете:')
print(f"Меня зовут {name}. Мне {age} лет. Проживаю в городе {city}.")
print('Меня зовут %s. Мне %d лет. Проживаю в городе %s.' % (name, age, city))
print('Меня зовут {}. Мне {} лет. Проживаю в городе {}.'.format(name, age, city))



