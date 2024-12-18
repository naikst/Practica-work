# Класс Product для описания товара
class Product:
    def __init__(self, name, weight, category):
        """
        Инициализатор для товара.
        :param name: Название товара (строка)
        :param weight: Вес товара (дробное число)
        :param category: Категория товара (строка)
        """
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """
        Метод для преобразования объекта Product в строку.
        Возвращает строку вида 'название, вес, категория'.
        """
        return f"{self.name}, {self.weight}, {self.category}"


# Класс Shop для управления магазином и хранения данных в файле
class Shop:
    __file_name = "products.txt"  # Имя файла для хранения данных о товарах

    def __init__(self):
        """
        Конструктор класса Shop. Проверяет, существует ли файл.
        Если файла нет, создает его.
        """
        try:
            with open(self.__file_name, "x", encoding="utf-8"):
                pass  # Просто создаем файл, если его нет
        except FileExistsError:
            pass  # Если файл уже существует, ничего не делаем

    def get_products(self):
        """
        Читает содержимое файла с товарами и возвращает строку со всеми продуктами.
        """
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return file.read().strip()  # Убираем лишние пробелы и переносы строк
        except FileNotFoundError:
            return ""  # Если файл не найден, возвращаем пустую строку

    def add(self, *products):
        """
        Добавляет новые продукты в магазин, если их ещё нет в файле.
        :param products: Произвольное количество объектов класса Product.
        """
        # Получаем список строк из файла
        existing_products = self.get_products().split("\n")

        # Открываем файл в режиме добавления
        with open(self.__file_name, "a", encoding="utf-8") as file:
            for product in products:
                product_str = str(product)  # Преобразуем объект Product в строку
                if product_str not in existing_products:
                    file.write(product_str + "\n")  # Добавляем в файл
                else:
                    print(f"Продукт {product.name} уже есть в магазине")  # Выводим сообщение


# Пример использования
if __name__ == "__main__":
    # Создаем объект магазина
    s1 = Shop()

    # Создаем несколько товаров
    p1 = Product("Potato", 50.5, "Vegetables")
    p2 = Product("Spaghetti", 3.4, "Groceries")
    p3 = Product("Potato", 5.5, "Vegetables")  # Товар с таким же названием, но другим весом

    print(p2)  # Ожидается: Spaghetti, 3.4, Groceries

    # Добавляем товары в магазин
    s1.add(p1, p2, p3)

    # Выводим содержимое файла с продуктами
    print(s1.get_products())