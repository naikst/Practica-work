def get_matrix(n, m, value):
    # Создаем пустой список для хранения строк матрицы
    matrix = []
    # Внешний цикл для создания строк матрицы
    for _ in range(n):
        # Создаем новую строку в виде пустого списка
        row = []
        # Внутренний цикл для заполнения строки значениями
        for _ in range(m):
            # Заполняем строку значениями
            row.append(value)
        # Добавляем заполненную строку в общую матрицу
        matrix.append(row)
        # Возвращаем общую матрицу
    return matrix


# Вызовы функции для тестирования
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
