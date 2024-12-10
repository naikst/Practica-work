class Vehicle:
    # Возможные цвета для автомобиля
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        # Инициализация объекта с характеристиками
        self.__owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        # Возвращает модель автомобиля
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        # Возвращает мощность двигателя в лошадиных силах
        return f'Мощность двигателя: {self.__engine_power} л.с.'

    def get_color(self):
        # Возвращает цвет автомобиля
        return f'Цвет: {self.__color}'

    @property
    def owner(self) -> str:
        # Получает имя владельца
        return self.__owner

    @owner.setter
    def owner(self, new_owner: str):
        self.__owner = new_owner  # Устанавливает нового владельца автомобиля

    def print_info(self):
        print(self.get_model())      # Выводит модель автомобиля
        print(self.get_horsepower()) # Выводит мощность двигателя
        print(self.get_color())      # Выводит цвет автомобиля
        print(f'Владелец: {self.__owner}') # Выводит владельца автомобиля

    def set_color(self, new_color:str):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color.lower()  # Изменяет цвет, если он разрешен
        else:
            print(f'Нельзя сменить цвет на {new_color}')  # Сообщение об ошибке, если цвет недопустим


class Sedan(Vehicle):
    # Класс Sedan, представляющий легковой автомобиль (дополнительная специфика)
    __PASSENGERS_LIMIT = 5  # Лимит пассажиров для этого автомобиля
    pass





# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')  # Создание нового автомобиля


# Изначальные свойства
vehicle1.print_info()  # Печать информации об автомобиле


# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')    # Пытаемся изменить цвет на розовый (не доступен)
vehicle1.set_color('BLACK')   # Изменяем цвет на черный (доступен)
vehicle1.owner = 'Vasyok'     # Изменяем владельца автомобиля


# Проверяем что поменялось
vehicle1.print_info()  # Печать обновленной информации об автомобиле