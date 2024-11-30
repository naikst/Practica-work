class Animals:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
        # меняется атрибут fed на True. В противном случае выводит на экран "<self.name> не съел <food.name>"

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:  # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
            # меняется атрибут alive на False.
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # В противном случае выводит на экран "<self.name> стал есть <food.name>"


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


#  #У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.


class Mammal(Animals):
    pass  # Наследует все от Animal без изменений


class Predator(Animals):
    pass  # Наследует все от Animal без изменений


class Flower(Plant):
    pass  # Наследует все от Animal без изменений


# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)  # Наследует все от Plant без изменений
        self.edible = True  # Наследует все от Plant без изменений


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
