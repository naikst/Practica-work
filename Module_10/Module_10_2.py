import threading
import time


class Knight(threading.Thread):
    # Общий атрибут для всех рыцарей
    enemies = 100  # Начальное количество врагов

    def __init__(self, name, power, lock):
        threading.Thread.__init__(self)  # Инициализация базового класса
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.days = 0  # Счетчик дней сражения

        # Блокировка для синхронизации вывода
        self.lock = lock

    def run(self):
        # При начале сражения выводим сообщение о нападении
        with self.lock:
            print(f"{self.name}, на нас напали!")

            # Пока есть враги
        while True:
            with self.lock:  # Блокировка доступа к общему ресурс
                if self.enemies <= 0:  # Если враги побеждены, выходим из цикла
                    break
                # Вывод сообщения о текущем состоянии сражения
                print(f"{self.name} сражается {self.days + 1} день(дня)..., осталось {self.enemies} воинов.")
                self.enemies -= self.power  # Уменьшаем количество врагов
                if self.enemies < 0:  # Если врагов стало меньше нуля
                    self.enemies = 0  # Устанавливаем количество врагов на 0

            time.sleep(1)  # Задержка на 1 секунду (символизируем день)
            self.days += 1  # Увеличиваем счетчик дней

        # Выводим сообщение о победе
        with self.lock:
            print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


# Создаем блокировку для синхронизации среди потоков
lock = threading.Lock()

# Создаём и запускаем двух рыцарей
first_knight = Knight('Sir Lancelot', 10, lock)
second_knight = Knight('Sir Galahad', 20, lock)

first_knight.start()  # Запускаем первый поток
second_knight.start()  # Запускаем второй поток

# Ожидаем завершения сражения обоих рыцарей
first_knight.join()
second_knight.join()

# Выводим сообщение об окончании битвы
print("Все битвы завершены!")