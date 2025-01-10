# Декоратор is_prime, который проверяет, является ли результат функции sum_three
def is_prime(func):
    def wrapper(a, b, c):  # Принимаем три аргумента (a, b, c)
        result = func(a, b, c)  # Вызываем функцию sum_three с аргументами


        # Проверка на простое число
        if result < 2:  # Числа меньше 2 не являются простыми
            print("Составное")
        else:
            is_prime_number = True  # Предполагаем, что число простое
            for i in range(2, result):  # Проверяем делители от 2 до result - 1
                if result % i == 0:  # Если число делится на i, оно не простое
                    is_prime_number = False
                    break
            if is_prime_number:
                print("Простое")
            else:
                print("Составное")

        return result  # Возвращаем результат функции sum_three

    return wrapper  # Возвращаем wrapper как новую функцию


# Функция sum_three, обёрнутая в декоратор is_prime
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Вызов функции
result = sum_three(2, 3, 6)  # Складываем числа 2, 3 и 6
print(result)  # Выводим результат