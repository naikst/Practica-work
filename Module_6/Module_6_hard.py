import math


class Figure:
    sides_count = 0  # Количество сторон, у Figure пока 0

    def __init__(self, color, *sides):
        self.filled = False  # Закрашена ли фигура
        self.__color = list(color)  # RGB цвет
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count  # _sides(список сторон (целые числа))

    def get_color(self):  # Получить цвет фигуры
        return self.__color  # возвращает цвет фигуры (RGB)

    def __is_valid_color(self, r, g, b):  # Проверка цвета
        # Проверка, что все значения цвета(r,g,b)- целый числа в диапазоне от 0 до 255
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):  # Установить цвет фигуры
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]  # # Устанавливаем новый цвет
        else:
            print('Неверный цвет')

    def __is_valid_sides(self, sides):  # Проверка стороны
        # Проверка, что все стороны - целые положительные числа, и их количество равно sides_count
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):  # Получить список сторон
        return self.__sides  # возвращает список сторон

    def set_sides(self, *new_sides):  # Установить список сторон
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)  # Устанавливаем новый список сторон
        else:
            print('Некорректное количество сторон, стороны остаются неизменными')


def __len__(self):  # Длина фигуры
    return sum(self.__sides)  # возвращает периметр фигуры


class Circle(Figure):
    sides_count = 1  # У круга одна сторона (длина окружности)

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        # Круг создаётся с помощью метода super()
        # super() - вызывает метод класса, который является базовым для данного класса
        self.__radius = circumference / (2 * math.pi)  # Вычисляем радиус на основе длины окружности

    def get_radius(self):
        return math.pi * self.__radius ** 2  # # Площадь круга

    def __len__(self):  # Периметр круга (длина окружности)
        return int(2 * math.pi * self.__radius)  # Возвращаем длину окружности


class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def get_square(self):  # Формула Герона для расчёта площади треугольника
        a, b, c = self.get_sides()  # Получаем стороны треугольника
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь по формуле Герона для треугольника


class Cube(Figure):  # class Куб
    sides_count = 12  # # У куба 12 рёбер

    def __init__(self, color, edge_length):
        super().__init__(color, *([edge_length]) * 12)  # Создаём куб с 12 одинаковыми рёбрами

    def get_volume(self):
        # Возвращаем объём куба
        edge_length = self.get_sides()[0]  # Все рёбра одинаковы
        return edge_length ** 3  # Объём куба


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
