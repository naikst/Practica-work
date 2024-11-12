def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, "равно", b)
    else:
        print(b, 'максимально')


printMax(3, 4)  # Прямая передача значений

x = 5
y = 7

printMax(x, y)  #передача переменных в качетсве аргументов
# Здесь мы определили функцию с именем printMax,  которая использует два параметра с именем a и b. Мы находим
# наибольшее число с применением простого оператора if..else и выводим это число. При первом вызове функций printMax
# мы напрямую передаём числа в качестве аргументов.Во втором случае мы вызываем функцию с переменными в качетсве
# аргументов. printMax(x, y) назначает значение аргумента х параметру а, а значение аргумента у -  параметру b. В
# обоих случаях функция printMax работает одинаково.
