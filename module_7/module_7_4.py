team1_num = 5  # Количество участников в команде "Мастера кода"
team2_num = 6  # Количество участников в команде "Волшебники данных"
score_1 = 40   # Количество решенных задач командой "Мастера кода"
score_2 = 42   # Количество решенных задач командой "Волшебники данных"
team1_time = 1552.512  # Время решения задач командой "Мастера кода" (в секундах)
team2_time = 2153.31451  # Время решения задач командой "Волшебники данных" (в секундах)
tasks_total = 82   # Общее количество задач
time_avg = 45.2  # Среднее время решения одной задачи (в секундах)
challenge_result = 'Победа команды Волшебники данных!'  # Изначальный результат битвы

# Использование %
print("В команде Мастера кода участников: %d!" % team1_num)  # Выводим количество участников в команде "Мастера кода"
print('Итого сегодня в команде участников: %d и %d!' % (team1_num, team2_num))  # Выводим общее количество участников в обеих командах

# Использование format()
print('Команда волшебники данные решили задач: {}!'.format(score_2))  # Выводим количество решенных задач командой "Волшебники данных"
print('Волшебники данных решили задачи за {:.3f}'.format(team1_time))  # Выводим время решения задач командой "Волшебники данных" с округлением до 3 знаков после запятой

# Использование f-строки
print(f'Команды решили {score_1} и {score_2} задач')  # Выводим количество решенных задач обеими командами
print(f'Результат битвы: {challenge_result}')  # Выводим текущий результат битвы

print(f'Сегодня было решено {tasks_total} задач, в среднем {time_avg} секунд на задачу')  # Выводим общее количество задач и среднее время решения одной задачи

# Определяем победителя битвы, основываясь на количестве решенных задач и времени решения
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'  # "Мастера кода" победили, если у них больше решенных задач, или если количество задач одинаковое, но они решили их быстрее
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'  # "Волшебники данных" победили, если у них больше решенных задач, или если количество задач одинаковое, но они решили их быстрее
else:
    challenge_result = 'Ничья!'  # В случае, если количество задач одинаковое, а время решения тоже, то объявляется ничья

print(f'Результат битвы: {challenge_result}')  # Выводим окончательный результат битвы