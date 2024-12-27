def personal_sum(numbers):  # принимает коллекцию чисел
    result = 0  # Переменная для хранения суммы чисел
    incorrect_data = 0  # Переменная для подсчёта некорректных данных (не числовых значений)


    for number in numbers: # # Перебираем каждый элемент в коллекции numbers
        try:
            # Пытаемся прибавить число к result
            # Если элемент не является числом, будет вызвано исключение TypeError
            result += number
        except TypeError: # Если возникло исключение TypeError, увеличиваем счётчик некорректных данных
            print(f"Некорректный тип данных для подсчёта суммы - {repr(number)}")
            incorrect_data += 1
    # В конце возвращаем кортеж из двух значений:
    # - сумма всех корректных чисел
    # - количество некорректных данных
    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Пытаемся вызвать функцию personal_sum для получения суммы и количества ошибок
        total, incorrect_data = personal_sum(numbers)
        # Возвращаем среднее арифметическое.
        # Среднее рассчитывается как сумма корректных чисел, делённая на количество этих чисел.
        # Общее количество чисел равно длине коллекции numbers минус количество некорректных данных.
        return total / (len(numbers) - incorrect_data)  # вычисление среднего
    # Обработка исключения, если деление на 0 (например, если все данные некорректны)
    except ZeroDivisionError:
        return 0  # Возвращаем 0, если делить не на что
    # Обработка случая, когда в функцию переданы некорректные типы данных (например, число вместо списка)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
