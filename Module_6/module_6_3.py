# Подключаем модуль random для работы с генерацией случайных чисел
import random

# Родительский класс Animal (Животное), от которого наследуются другие классы
class Animal:
    # Атрибут указывает, что животное живое
    live = True
    # Атрибут звука, который издает животное (должен быть установлен наследниками)
    sound = None
    # Степень опасности животного, используется для проверки его агрессивности
    _DEGREE_OF_DANGER = 0
    # Координаты местоположения животного в формате [x, y, z]
    _cords = [0, 0, 0]
    # Скорость передвижения животного
    speed = 0

    # Конструктор, который задает скорость животного
    def __init__(self, speed):
        self.speed = speed

    # Метод для перемещения животного по осям x, y, z с учетом скорости
    def move(self, dx, dy, dz):
        # Учитываем скорость при изменении координат
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        # Проверяем, если животное "уходит" ниже допустимой глубины
        if new_z < 0:
            print("t's too deep, i can't dive :(")
        else:
            # Обновляем координаты животного
            self._cords = [new_x, new_y, new_z]

    # Метод для вывода текущих координат животного
    def get_cords(self):
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')

    # Метод атаки, который проверяет степень опасности
    def attack(self):
        if self._DEGREE_OF_DANGER <= 5:
            # Если животное не опасно, оно заявляет о своей мирности
            print("Sorry, i'm peaceful :)")
        else:
            # Если животное опасно, оно атакует
            print("Be careful, i'm attacking you 0_0")

    # Метод, который позволяет животному "говорить" (выводить его звук)
    def speak(self):
         print(self.sound)




# Класс Bird (Птица), наследуется от Animal
class Bird(Animal):
    # Птицы имеют клюв (по умолчанию)
    beak = True

    # Метод откладывания яиц, генерирует случайное количество яиц
    def lay_eggs(self):
        eggs = random.randint(1, 4)  # Генерируем случайное число яиц от 1 до 4
        print(f'Here are(is) {eggs} egg{"s" if eggs != 1 else ""} for you')

# Класс AquaticAnimal (Водное животное), наследуется от Animal
class AquaticAnimal(Animal):
    # У водных животных степень опасности по умолчанию равна 3
    _DEGREE_OF_DANGER = 3

    # Метод погружения животного под воду
    def dive_in(self, dz):
        dz = abs(dz)  # Берем модуль глубины, чтобы избежать негативных значений
        # Скорость уменьшается в 2 раза при погружении
        self.speed /= 2
        # Уменьшаем значение координаты z, чтобы показать погружение
        self._cords[2] -= dz
        # Проверяем, если значение координаты z стало меньше нуля
        if self._cords[2] < 0:
            self._cords[2] = 0  # Координата z не может быть ниже 0
            print("Я слишком глубоко, не могу погрузиться :(")



# Класс PoisonousAnimal (Ядовитое животное), наследуется от Animal
class PoisonousAnimal(Animal):
    # Уровень опасности у ядовитых животных составляет 8
    _DEGREE_OF_DANGER = 8

# Класс Duckbill (Утконос) - пример множественного наследования от PoisonousAnimal, AquaticAnimal и Bird
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    # Утконос издает специфический звук
    sound = "Click-click-click"

    # Конструктор класса, который вызывает конструктор родительского класса
    def __init__(self, speed):
        super().__init__(speed)







# Создаем экземпляр класса Duckbill с начальной скоростью 10
db = Duckbill(10)

# Проверяем, жив ли утконос
print(db.live)
# Проверяем наличие клюва у утконоса
print(db.beak)

# Утконос издает звук
db.speak()
# Проверяем поведение утконоса при атаке
db.attack()

# Перемещаем утконоса
db.move(1, 2, 3)
# Получаем текущие координаты
db.get_cords()
# Утконос погружается под воду
db.dive_in(6)
# Получаем обновленные координаты
db.get_cords()

# Утконос откладывает яйца
db.lay_eggs()