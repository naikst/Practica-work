def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


# Пример выполнения программы:
print(apply_all_func([6, 20, 15, 9], max, min))  # Вывод: {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))  # Вывод: {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}



