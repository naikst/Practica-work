# lambda-функцию для сравнения символов двух строк по позициям
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Создаем список, где каждый элемент - результат сравнения символов из first и second
result = list(map(lambda x, y: x == y, first, second ))

#Выводим результат
print(result)



# функция get_advanced_writer(file_name), которая возвращает функцию write_everything(*data_set),
# и записывает данные в файл.
def get_advanced_write(file_name):
    # Внутренняя функция, которая принимает любое количество данных
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data))
    return write_everything

# Создаем функцию, ждя записи в файл "example.txt"
write = get_advanced_write('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


from random import choice

#  класс MysticBall, объекты которого могут быть вызваны как функции для случайного выбора слова.
class MysticBall:
    def __init__(self, *words):
        # Инициализация атрибута words списком переданных слов
        self.words = words

    def __call__(self):
        # Возращает случайное слово из списка
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())