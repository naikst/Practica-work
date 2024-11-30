d = 7  # Глобальная переменная


def square(x):
    d = x ** 2  # Локальная переменная d в функции square

    def even(x):
        nonlocal d  # nonlocal говорит, что нужно использовать переменную d из функции square
        d = x / 2  # Изменяем значение d
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')

    even(x)  # Вызов вложенной функции even
    return d  # Возвращаем значение переменной d после ее изменения в even


a = 5  # Глобальная переменная
b = square(4)  # Вызов функции square
print(a)  # Выведет глобальную переменную a (5)
print(b)  # Выведет результат работы функции square
