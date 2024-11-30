first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Все', 3, 'числа равны между собой')
elif first == second or second == third or third == first:
    print(2, 'числа равны между собой')
else:
    print('Обнаружено', 0, 'равных между собой чисел')
