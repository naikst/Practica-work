class Animal:
    alive = True  # Живое существо, изначально живое
    fed = False  # Изначально не накормленное
    name = ""  # Имя животного

    # Конструктор, который задаёт имя животного
    def __init__(self, name):
        self.name = name

    # Метод, позволяющий животному есть
    def eat(self, food):
        # Проверяем, съедобно ли
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True  # Животное накормлено
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # Если не съедобно, то животное умирает


class Planet:
    edible = False  # Объекты по умолчанию не съедобны
    name = ""  # Имя объекта

    # Задаём имя объекта
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    # Млекопитающее, наследует свойства животного
    pass


class Predator(Animal):
    # Хищник, наследует свойства животного
    pass


class Flower(Planet):
    edible = True  # Цветок съедобен

    def __init__(self, name):
        super().__init__(name)

class Fruit(Planet):
    def __init__(self, name):
        super().__init__(name)


# Создание экземпляров классов и взаимодействие между ними
a1 = Predator('Волк с Уолл-Стрит')  # Хищник
a2 = Mammal('Хатико')  # Млекопитающее
p1 = Flower('Цветик семицветик')  # Съедобный цветок
p2 = Fruit('Заводной апельсин')  # Фрукт

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Хищник пытается съесть цветок
a1.eat(p1)

# Млекопитающее съедает фрукт
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Итоги: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

