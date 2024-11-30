# Переменное число параметров


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)

    # проход по всем элементам словаря
    for first_part, secong_part in phonebook.items():
        print(first_part, secong_part)


print(total(10, 1, 2, 3, Jack=1123, john=2231, Inge=1560))

# Как это работает: Когда мы обьявляем параметр со звёздочкой(*numbers)  все позиционные аргументы начиная с этой
# позиций и до конца будут собраны в кортеж под этим именим numbers. Аналогично, когда мы обьявляем параметры с двумя
# звёздочками(**phonebook), все ключевые аргументы начиная с этой позиций и до конца будут собраны в словарь под этим
# именем phonebook.
