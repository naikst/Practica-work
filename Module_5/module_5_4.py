class House:
    houses_history = []  # Список для хранения истории домов

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  # Создаём новый объект
        cls.houses_history.append(args[0])  # Добавляем объект в историю
        return instance

    def __init__(self, name, number_of_floors):
        # Конструктор класса House
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Метод, который вызывается при удалении объекта
        print(f"'{self.name}' был снесён, но он останется в истории")

    def __str__(self):
        return f"Дом '{self.name}' с {self.number_of_floors} этажами"

    def __repr__(self):
        # Возвращаем строковое представление объекта для вывода в списке
        return f"'{self.name}'"


# Создаём объекты
h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем объекты
del h2
del h3

# Выводим историю домов
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
