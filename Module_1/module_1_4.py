my_string = input('Введите слово: ')  # # Запрос на ввод строки от пользователя

print('Количество символов введённого текста: ', len(my_string))  # Вывод количества символов введённого текста

print('В верхнем регистре: ', my_string.upper())  # Вывод строки в верхнем регистре

print('В нижнем регистре: ', my_string.lower())  # Вывод строки в нижнем регистре

print('Без пробелов: ', my_string.replace(" ", ""))  # Вывод строки без пробелов

print("Первый символ: ", my_string[0])  # Вывод первого символа

print("Последний символ:", my_string[-1])  # Вывод последнего символа