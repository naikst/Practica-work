def get_matrix(n, m, value):
    matrix = []         # Создали пустой список matrix внутри функции get_matrix.
    for row in range(n):     #первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix.append([])    #В первом цикле добавляем пустой список в список matrix.
        for col in range(m):  #во втором(внутренний) цикле for для кол-ва столбцов матрицы, m повторов.
            matrix[row].append(value)   #Во втором цикле пополнили ранее добавленный пустой список значениями value.

    return matrix # После всех циклов вернуть значение переменной matrix.

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
 # результат работы функции get_matrix.
