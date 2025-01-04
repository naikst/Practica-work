# Пользовательский класс исключения StepValueError, который наследует от ValueError
class StepValueError(ValueError):
    pass

class Iterator:
    """
    Создаем класс Iterator, который обладает следующими свойствами:

    Атрибуты объекта:
    start - целое число, с которого начинается итерация.
    stop - целое число, на котором заканчивается итерация.
    step - шаг, с которым совершается итерация.
    pointer - указывает на текущее число в итерации (изначально start)
    """
    def __init__(self, start, stop, step=1):  # Инициализируем с параметрами
        self.start = start  # Задаем начальное значение итерации
        self.stop = stop    # Задаем конечное значение итерации
        self.step = step    # Задаем шаг итерации
        if self.step == 0:  # Проверяем шаг на равенство 0
            raise StepValueError('шаг не может быть равен 0')  # Если шаг 0, бросаем исключение
        self.pointer = self.start  # Устанавливаем указатель на значение start

    # метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self

    # Метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step
    # итерация завершится либо когда pointer станет больше stop, либо меньше stop.
    def __next__(self):
        if self.step > 0:  # Если шаг положительный
            if self.pointer > self.stop:  # Если указатель превысил stop
                raise StopIteration  # Останавливаем итерацию
            else:
                result = self.pointer  # Сохраняем текущее значение
                self.pointer += self.step  # Увеличиваем указатель на шаг
                return result  # Возвращаем текущее значение
        else:  # Если шаг отрицательный
            if self.pointer < self.stop:  # Если указатель ниже stop
                raise StopIteration  # Останавливаем итерацию
            else:
                result = self.pointer  # Сохраняем текущее значение
                self.pointer += self.step  # Уменьшаем указатель на шаг
                return result  # Возвращаем текущее значение



# Пример выполняемого кода:
try:
    # Пробуем создать итератор с нулевым шагом
    iter1 = Iterator(100, 200, 0)  # Это вызовет исключение
    for i in iter1:
        print(i, end=' ')  # Не будет выполнено
except StepValueError:
    print('Шаг указан неверно')  # Обработка исключения

# Создаём различные итераторы
iter2 = Iterator(-5, 1)  # Итерация от -5 до 1
iter3 = Iterator(6, 15, 2)  # Итерация от 6 до 15 с шагом 2
iter4 = Iterator(5, 1, -1)  # Итерация от 5 до 1 с шагом -1
iter5 = Iterator(10, 1)  # Итерация от 10 до 1 с шагом -1 (уменьшаем)

# Выполнение итерации для каждого созданного итератора
for i in iter2:
    print(i, end=' ')  # Вывод: -5 -4 -3 -2 -1 0 1
print()  # Переход на новую строку

for i in iter3:
    print(i, end=' ')  # Вывод: 6 8 10 12 14
print()

for i in iter4:
    print(i, end=' ')  # Вывод: 5 4 3 2 1
print()

for i in iter5:
    print(i, end=' ')  # Вывод: 10 9 8 7 6 5 4 3 2
print()