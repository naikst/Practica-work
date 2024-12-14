import math

class Figure:
    sides_count = 0  # Количество сторон фигуры, задаётся в дочерних классах

    def __init__(self, color, *sides):
        # Если sides не задано или количество сторон не совпадает с sides_count,
        # создаётся массив с длинами сторон, равными 1.
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.__color = list(color)  # RGB код цвета
        self.filled = False  # Закрашен ли объект (по умолчанию False)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Проверяет, что каждый компонент цвета (r, g, b) — целое число от 0 до 255.
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        # Если цвет корректен, он обновляется, иначе выводится предупреждение.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректный цвет. Цвет остаётся прежним.")

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        # Проверяет количество и значения сторон (значения должны быть положительными числами).
        # В случае ошибки выводится предупреждение.
        if len(new_sides) == self.sides_count and all(isinstance(side, (int, float)) and side > 0 for side in new_sides):
            self.__sides = list(new_sides)
        else:
            print("Неверное количество сторон или некорректные значения.")

    def __len__(self):
        # Возвращает периметр (сумму длин всех сторон).
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1  # У круга одна сторона, обозначающая длину окружности

    def __init__(self, color, circumference):
        # Передаём длину окружности через конструктор базового класса.
        super().__init__(color, circumference)

    @property
    def radius(self):
        # Радиус рассчитывается на основе длины окружности, полученной через get_sides().
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        # Возвращает площадь круга с использованием формулы πr².
        r = self.radius
        return math.pi * r ** 2


class Triangle(Figure):
    sides_count = 3  # Треугольник всегда имеет три стороны

    def __init__(self, color, *sides):
        # Передаём три стороны треугольника через конструктор базового класса.
        super().__init__(color, *sides)

    def get_square(self):
        # Рассчитывает площадь треугольника по формуле Герона.
        a, b, c = self.get_sides()
        p = sum(self.get_sides()) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12  # У куба всегда 12 рёбер

    def __init__(self, color, edge_length):
        # Передаём 12 одинаковых рёбер с длиной edge_length через конструктор базового класса.
        super().__init__(color, *(edge_length,) * 12)

    def get_volume(self):
        # Возвращает объём куба, вычисленный на основе длины рёбер.
        edge = self.get_sides()[0]
        return edge ** 3


# Проверка
circle1 = Circle((200, 200, 100), 10)  # Белый цвет, длина окружности 10
cube1 = Cube((222, 35, 130), 6)  # Синий цвет, длина ребра 6

# Изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # [55, 66, 77]

cube1.set_color(300, 70, 15)  # Некорректный цвет
print(cube1.get_color())  # [222, 35, 130]

# Изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Ошибка: неверное количество сторон
print(cube1.get_sides())  # [6, 6, ..., 6] (12 раз)

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Периметр круга (длина окружности):
print(len(circle1))  # 10

# Объём куба:
print(cube1.get_volume())