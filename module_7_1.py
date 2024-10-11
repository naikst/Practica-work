# Конструктор класса, который инициализирует атрибуты продукта
class Product:
    def __init__(self, name, weight, category):
        self.name = name  # Название продукта (строка)
        self.weight = weight  # Вес продукта (число с плавающей точкой)
        self.category = category  # Категория продукта (строка)

    # Метод для представления объекта в виде строки
    def __str__(self):
        # Возвращает строку вида '<название>, <вес>, <категория>'
        return f'{self.name}, {self.weight}, {self.category}'

# Класс Shop для управления магазином и работы с файлами
class Shop:
    __file_name = 'products.txt'  # Инкапсулированный атрибут с именем файла

    # Конструктор класса Shop для работы с файлом
    def __init__(self):
        # Проверка на существование файла и его создание при необходимости
        try:
            with open(self.__file_name, 'x', encoding='utf-8') as file:
                pass
        except FileExistsError:
            pass

    def get_products(self):  # Метод для получения списка продуктов
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()  # Читаем и возвращаем содержимое файла
        except FileNotFoundError:
            # Если файл не существует, возвращаем пустую строку
            return ''

    def add(self, *products):
        # Получаем все продукты, которые уже есть в файле
        existing_products = self.get_products().split('\n')
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                product_str = str(product)  # Преобразуем объект Product в строку
                if product_str not in existing_products:
                    # Если продукта нет в файле, добавляем его
                    file.write(product_str + '\n')
                else:
                    # Если продукт уже есть, выводим сообщение
                    print(f'Продукт {product_str} уже есть в магазине')

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())