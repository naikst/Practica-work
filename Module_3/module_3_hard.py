def calculate_structure_sum(data_structure):
    total_sum: int = 0  # Здесь будет храниться итоговая сумма

    # Внутренняя рекурсивная функция для обработки всех элементов
    def recursive_sum(item):
        nonlocal total_sum  # Используем переменную из внешней функций.

        # Проверяем тип элемента
        if isinstance(item, int):  # Если это число
            total_sum += item  # Добавляем к сумме
        elif isinstance(item, str):  # Если это строка
            total_sum += len(item)  # Добавляем длину строки к сумме
        elif isinstance(item, (list, tuple, set)):  # Добавляем список, кортеж или множество
            for elem in item:  # Обрабатываем каждый элемент в структуре
                recursive_sum(elem)  # Рекурсивно вызываем для каждого элемента
        elif isinstance(item, dict):  # Если это слово
            for key, value in item.items():  # Проходим по ключам и значениям
                recursive_sum(key)  # Обрабатываем ключ
                recursive_sum(value)  # Обрабатываем значение

    recursive_sum(data_structure)  # Запускаем рекурсивную обработку с исходным структурой

    return total_sum  # Возвращаем итоговую сумму


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
