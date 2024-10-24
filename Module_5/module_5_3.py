class House:  # Определение класса House (Дом)
    def __init__(self, name, number_of_floors):
        # Это конструктор класса. Он вызывается при создании нового объекта House
        # name - название дома, number_of_floors - количество этажей
        self.name = name  # Сохраняем название дома как атрибут объекта
        self.number_of_floors = number_of_floors  # Сохраняем количество этажей как атрибут объекта

    def go_to(self, new_floor):
        # Метод для "перемещения" лифта на новый этаж
        # new_floor - номер этажа, на который нужно "переместиться"
        if 1 <= new_floor <= self.number_of_floors:
            # Проверяем, что новый этаж находится в допустимом диапазоне
            for floor in range(1, new_floor + 1):
                # Цикл от 1 до нового этажа (включительно)
                print(floor)  # Выводим номер каждого этажа
        else:
            # Если этаж вне допустимого диапазона
            print("Такого этажа не существует")

    def __len__(self):
        # Специальный метод, который вызывается при преобразовании объекта в число
        # Например, при использовании функции len(house_object)
        return self.number_of_floors  # Возвращает количество этажей дома
        # В данном случае, число этажей дома будет возвращено из атрибута number_of_floors
        # Этот метод может использоваться в циклах и других условиях, когда требуется получить число свойств объекта

    def __str__(self):
        # Специальный метод, который вызывается при преобразовании объекта в строку
        # Например, при использовании функции print(house_object)
        return f"Дом '{self.name}' с {self.number_of_floors} этажами"
        # Возвращает строку с информацией о доме

    def __eq__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора ==
            return self.number_of_floors == other.number_of_floors  # Возвращает True, если количество этажей совпадает
        return False  # Возвращает False, если количество этажей не совпадает

    def __lt__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора <
            return self.number_of_floors < other.number_of_floors  # Возвращает True, если количество этажей меньше
        return False  # Возвращает False, если количество этажей не меньше

    def __le__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора <=
            return self.number_of_floors <= other.number_of_floors  # Возвращает True, если количество этажей меньше или
        # равно
        return False  # Возвращает False, если количество этажей не меньше

    def __gt__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора >
            return self.number_of_floors > other.number_of_floors  # Возвращает True, если количество этажей больше
        return False  # Возвращает False, если количество этажей не больше

    def __ge__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора >=
            return self.number_of_floors >= other.number_of_floors  # Возвращает True, если количество этажей больше или
            # равно
        return False  # Возвращает False, если количество этажей не больше

    def __ne__(self, other):
        # Специальный метод, который вызывается при сравнении двух объектов
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора!=
            return self.number_of_floors != other.number_of_floors  # Возвращает True, если количество этажей не равно
        return False  # Возвращает False, если количество этажей равно

    def __add__(self, value):
        # Специальный метод, который вызывается при сложении двух объектов
        if isinstance(value, int):  # Проверяем, является ли value целым числом
            # Например, при использовании оператора +
            return House(self.name, self.number_of_floors + value)  # Возвращает новый объект House с новым названием и
            # суммарным кол-вом этажей
        return NotImplemented  # Возвращает NotImplemented, если сложение невозможно (например, для House и str)

    def __radd__(self, value):
        # Специальный метод, который вызывается при сложении числа с объектом
        return self.__add__(value)  # Вызывает __add__ с обратным порядком операндов

    def __iadd__(self, value):
        # Метод __iadd__ предназначен для изменения объекта "на месте" при использовании оператора +=.
        if isinstance(value, int):  # Проверяем, является ли value целым числом
            # Например, при использовании оператора +=
            self.number_of_floors += value  # Изменяет количество этажей
        return self  # Возвращает текущий объект


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)  # __eq__
h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)
h1 += 10  # __iadd__
print(h1)
h2 = 10 + h2  # __radd__
print(h2)
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
