import os  # для работы с файловой системой.
import time  # для форматирования времени.

# Указываем директорию для обхода
directory = r"K:\Practical_work\new-feature" # Проход по всем файлам и папкам в указанной директории

for root, dirs, files in os.walk(directory):
    # Функция os.walk() позволяет рекурсивно обходить все файлы и папки в указанной директории. Она возвращает кортеж из трех элементов
    # root, dirs, files.
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)  # преобразует время из формата UNIX в локальное время.
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # форматирует дату в привычный вид "день.месяц.год часы:минуты".
        filesize = os.path.getsize(filepath)  # возвращает размер файла в байтах.
        relative_path = os.path.relpath(filepath, directory)
        print(f'Обнаружен файл: {file}, Путь: .\\{relative_path}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория:.')





