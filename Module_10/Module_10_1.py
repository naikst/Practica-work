import threading
import time
from datetime import timedelta  # Для форматирования времени


def wite_words(word_count, file_name):

    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)  # Задержка в 0.1 секунду
    print(f'Завершилась запись в файл {file_name}')


# Взятие текущего времени перед запуском функций
start_time_func = time.time()

# Запуск функций с аргументами из задачи
wite_words(word_count=10, file_name='example1.txt')
wite_words(word_count=30, file_name='example2.txt')
wite_words(word_count=200, file_name='example3.txt')
wite_words(word_count=100, file_name='example4.txt')

# Взятие текущего времени после завершения функций
end_time_func = time.time()

# Вывод разницы начала и конца работы функций
print(f'Время выполнения функций: {timedelta(seconds=end_time_func - start_time_func)}')

# Записываем текущее время перед запуском потоков
start_time_thread = time.time()

# Создание и запуск потоков с аргументами из задачи
thread_1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

# Запуск потоков
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# Ожидание завершения всех потоков
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

# Записываем текущее время после завершения всех потоков
end_time_thread = time.time()

# Вычисляем, сколько времени заняло выполнение всех потоков, и выводим результат
print(f'Время выполнения потоков: {timedelta(seconds=end_time_thread - start_time_thread)}')