calls = 0   # Переменная calls используется для подсчета количества вызовов функций string_info и is_contains.


def count_calls():  # функцию count_calls изменять в ней значение переменной calls. Эта функция
    # вызывается в остальных двух функциях. Функция count_calls увеличивает calls на 1 каждый раз, когда она вызывается.
    global calls  # Для использования глобальной переменной внутри функции  оператор global.
    calls += 1


def string_info(string):  # Функция string_info обрабатывает строку и возвращает информацию о ней, вызывая при этом
    # count_calls.
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):  # Функция is_contains проверяет наличие строки в списке, игнорируя регистр,
    # и также вызывает count_calls.
    count_calls()
    string_lower = string.lower()  # Проверяет, содержится ли string в list_to_search, игнорируя регистр букв. Для
    # этого приводим обе строки к нижнему регистру(string_lower)
    list_to_search_lower = [item.lower() for item in list_to_search]
    return string_lower in list_to_search_lower


# После выполнения программы выводится общее количество вызовов функций через переменную calls.

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
