class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message  # Устанавливаем сообщение об ошибке
        super().__init__(self.message)  # Передаём сообщение базовому классу

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message  # Устанавливаем сообщение об ошибке
        super().__init__(self.message)  # Передаём сообщение базовому классу


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Сохраняем модель машины
        # Проверяем VIN-номер
        if self.__is_valid_vin(vin):
            self.__vin = vin  # Сохраняем VIN, если он корректен
        # Проверяем номера машины
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # Сохраняем номера, если они корректны

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):  # Проверяем, что VIN — целое число
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not (1000000 <= vin <= 9999999):  # Проверяем диапазон VIN
            raise IncorrectVinNumber('Неверный диапазон vin номера')
        return True  # Если всё хорошо, возвращаем True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):  # Проверяем, что номера — строка
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:  # Проверяем длину номера
            raise IncorrectCarNumbers('Неверная длина номера')
        return True  # Если всё хорошо, возвращаем True
    # Пример выполняемого кода:

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
     print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
        print(exc.message)
else:
    print(f'{third.model} успешно создан')
