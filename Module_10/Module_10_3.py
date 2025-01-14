import threading
import time
import random

# Создаем класс Bank
class Bank:
    # Инициализируем конструктор класса
    def __init__(self, balance):
        self.balance = balance  # Баланс банка
        self.lock = threading.Lock()  # Замок для синхронизации доступа к балансу
        self.condition = threading.Condition(self.lock)  # Условная переменная для блокировки/разблокировки

    # Метод deposit
    def deposit(self):
        # Выполняем 100 транзакций пополнения
        for _ in range(100):
            # Получаем случайное число от 50 до 500
            amount = random.randint(50, 500)
            # Блокируем доступ к балансу
            with self.lock:
                # Увеличиваем баланс на случайное число
                self.balance += amount
                # Выводим информацию о пополнении и текущем балансе
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                # Если баланс больше или равен 500, уведомляем все потоки
                if self.balance >= 500:
                    self.condition.notify_all()
            # Устанавливаем задержку в 0.001 секунды
            time.sleep(0.001)

    # Метод take
    def take(self):
        # Выполняем 100 транзакций снятия
        for _ in range(100):
            # Получаем случайное число от 50 до 500
            amount = random.randint(50, 500)
            # Блокируем доступ к балансу
            with self.lock:
                # Выводим сообщение о запросе снятия
                print(f'Запрос на {amount}')
                # Если средств недостаточно, ждем
                while amount > self.balance:
                    print('Запрос отклонён, недостаточно средств. Ожидание...')
                    # Блокируем поток до уведомления
                    self.condition.wait()
                # Уменьшаем баланс на случайное число
                self.balance -= amount
                # Выводим информацию о снятии и текущем балансе
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            # Устанавливаем задержку в 0.001 секунды
            time.sleep(0.001)

# Создаем объект класса Bank с начальным балансом 0
bk = Bank(0)

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')



