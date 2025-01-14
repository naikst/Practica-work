import os
import time

# Указываем путь к директории, которую мы хотим обойти
directory = r"D:\Practices\module_7"

# Обходим директорию с помощью os.walk
for root, dirs, files in os.walk(directory):
    # Для каждого файла в директории
    for file in files:
        # Получаем полный путь к файлу
        filepath = os.path.join(root, file)
        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        # Форматируем время в удобочитаемый формат
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # Получаем размер файла
        filesize = os.path.getsize(filepath)
        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

