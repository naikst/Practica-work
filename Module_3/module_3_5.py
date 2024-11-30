def get_multiplied_digits(number):  # функцию get_multiplied_digits и параметр number в ней.
    str_number = str(number)  # Преобразуем число в строку
    # Базовый случай: если длина строки 1, возвращаем само число
    if len(str_number) == 1:  # Проверка if len(str_number) == 1: гарантирует, что когда у нас осталась одна цифра,
        # функция возвращает эту цифру, завершая рекурсию.
        return int(str_number)

    # Получаем первую цифру числа
    first = int(str_number[0])

    # Рекурсивный вызов функции для оставшейся части числа
    return first * get_multiplied_digits(int(str_number[1:]))  # первая цифра умножается на результат рекурсивного
    # вызова функции для остальной части числа.


# Вызов функции с числом 40203
result = get_multiplied_digits(40203)
print(result)
