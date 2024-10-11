from math import inf


def divide(first, second):
    if second == 0:
        return inf  # Возвращаем бесконечность, если второй аргумент 0
    else:
        return first / second


