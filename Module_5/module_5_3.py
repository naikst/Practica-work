class House:  # Определение класса House (Дом)
    def __init__(self, name, number_of_floors):
        # Это как у дома имя и количество этажей сразу запоминаются, когда новый дом строится.
        self.name = name  # Сохраняем название дома как атрибут объекта
        self.number_of_floors = number_of_floors  # Сохраняем количество этажей как атрибут объекта

    def go_to(self, new_floor):
        # Лифт едет на нужный этаж — вот мы и программируем, на какой.
        if 1 <= new_floor <= self.number_of_floors:
            # Проверяем, что новый этаж находится в допустимом диапазоне
            for floor in range(1, new_floor + 1):
                # Цикл от 1 до нового этажа (включительно)
                print(floor)  # Выводим номер каждого этажа
        else:
            # Если этаж вне допустимого диапазона
            print("Такого этажа не существует")

    def __len__(self):
        # Когда нужно узнать, сколько этажей у дома, можно просто спросить.
        return self.number_of_floors  # Возвращает количество этажей дома
        # В данном случае, число этажей дома будет возвращено из атрибута number_of_floors
        # Этот метод может использоваться в циклах и других условиях, когда требуется получить число свойств объекта

    def __str__(self):
        # Превращаем дом в слова: как зовут и сколько этажей.
        return f"Название: '{self.name}', с кол-во этажей: {self.number_of_floors}"
        # Возвращает строку с информацией о доме

    def __eq__(self, other):
        # Сравниваем дома: одинаковое ли количество этажей?
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора ==
            return self.number_of_floors == other.number_of_floors  # Возвращает True, если количество этажей совпадает

    def __lt__(self, other):
        # Узнаём, у какого дома этажей меньше.
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора <
            return self.number_of_floors < other.number_of_floors  # Возвращает True, если количество этажей меньше
        return False  # Возвращает False, если количество этажей не меньше

    def __le__(self, other):
        # Проверяем: у дома этажей меньше или столько же?
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора <=
            return self.number_of_floors <= other.number_of_floors  # Возвращает True, если количество этажей меньше или
        # равно

    def __gt__(self, other):
        # Выясняем, у кого дом выше по этажности.
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора >
            return self.number_of_floors > other.number_of_floors  # Возвращает True, если количество этажей больше
        return False  # Возвращает False, если количество этажей не больше

    def __ge__(self, other):
        # Смотрим: количество этажей больше или равно?
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора >=
            return self.number_of_floors >= other.number_of_floors  # Возвращает True, если количество этажей больше или
        # равно

    def __ne__(self, other):
        # Проверка на неравенство этажей у домов.
        if isinstance(other, House):  # Проверяем, является ли other объектом House
            # Например, при использовании оператора!=
            return self.number_of_floors != other.number_of_floors  # Возвращает True, если количество этажей не совпадает
        return False  # Возвращает False, если количество этажей не совпадает

    def __add__(self, value):
        # Добавляем этажи к дому — строим выше.
        if isinstance(value, int):  # Проверяем, является ли value числом
            # Например, при использовании оператора +
            return House(self.name,
                         self.number_of_floors + value)  # Возвращает новый объект House с новым количеством этажей
        return NotImplemented  # Возвращает NotImplemented, если операция невозможна

    def __iadd__(self, value):
        # Добавляем этажи нашему дому, делая его выше.
        if isinstance(value, int):  # Проверяем, является ли value числом
            # Например, при использовании оператора +=
            self.number_of_floors += value  # Изменяем количество этажей объекта
            return self  # Возвращаем измененный объект
        return NotImplemented  # Возвращает NotImplemented, если операция невозможна

    def __radd__(self, value):
        # Прибавляем этажи, если их число первым стоит.
        if isinstance(value, int):  # Проверяем, является ли value числом
            # Например, при использовании оператора +
            return House(self.name,
                         value + self.number_of_floors)  # Возвращает новый объект House с новым количеством этажей
        return NotImplemented  # Возвращает NotImplemented, если операция невозможна


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
