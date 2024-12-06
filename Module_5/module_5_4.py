# Класс House: представляет собой дом, который имеет имя и количество этажей, и позволяет выполнять различные операции.
class House:  # Определение класса House (Дом)
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if args:
            # Проверяем, если есть какие-то аргументы при создании нового объекта
            cls.houses_history.append(args[0])  # Добавляем объект в историю домов
        return instance

    def __init__(self, name, number_of_floors):
        # Это конструктор, в котором у дома запоминаются его имя и количество этажей, когда создается новый объект дома.
        self.name = name  # Сохраняем название дома как атрибут объекта
        self.number_of_floors = number_of_floors  # Сохраняем количество этажей как атрибут объекта

    def go_to(self, new_floor):
        # Метод позволяет подняться на указанный этаж, проверяя при этом допустимость этажа.
        if 1 <= new_floor <= self.number_of_floors:
            # Проверяем, что запрашиваемый этаж в пределах количества этажей дома
            for floor in range(1, new_floor + 1):
                # Печатаем номер каждого этажа по пути до нужного
                print(floor)  # Выводим номер каждого этажа
        else:
            # Сообщаем, если запрашиваемый этаж за пределами возможных
            print("Такого этажа не существует")

    def __del__(self):
        print(f"'{self.name}' снесён, но он останется в историй")  # Выводим сообщение об удалении дома

    def __str__(self):
        # Метод преобразует объект дома в текстовую форму, показывая его имя и количество этажей.
        return f"Название: '{self.name}', с кол-во этажей: {self.number_of_floors}"
        # Возвращает строку с информацией о доме


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов

del h2
del h3

print(House.houses_history)
