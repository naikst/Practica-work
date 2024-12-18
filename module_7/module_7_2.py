def custom_write(file_name, strings):
    """
        Записывает строки в файл и возвращает словарь с позициями строк.

        :param file_name: Имя файла для записи (строка).
        :param strings: Список строк для записи (список строк).
        :return: Словарь с позициями строк.
        """
    with open(file_name, 'w', encoding='utf-8') as f:  # тут будет запись строк
        strings_positions = {}  # создаем словарь для хранения позиций
        line_number = 1  # счетчик строк, начинается с 1
        for line in strings: #Цикл по строкам и запись их в файл
            byte_position = f.tell()  # узнаем позицию до записи строки
            f.write(line + '\n')  # Записывать в файл file_name все строки из списка strings, каждая на новой строке.
            # После каждой строки будет закрываться новая строка.
            strings_positions[(line_number, byte_position)] = line  # сохраняем позицию и строку
            line_number += 1
    return strings_positions  # Возвращаем словарь с позициями и строками


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
