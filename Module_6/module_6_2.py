class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, model, engine_power, color, owner):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = owner

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        print(f"Цвет: {self.__color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
