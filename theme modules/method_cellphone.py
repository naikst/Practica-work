# Класс CellPhone содержит данные о сотовом телефоне

class CellPhone:

    # метод __init__ инициализирует атрибуты модели, производителя и цены
    def __init__(self, tecno, model_type, price):
        self.__model = model_type
        self.__tecno = tecno  # Исправлено имя атрибута
        self.__price = price

    # метод set_model_type принимает аргумент для
    # типа модели телефона
    def set_model_type(self, model_type):
        self.__model = model_type

    # метод ret_tecno принимает аргумент для
    # производителя телефона
    def ret_tecno(self, tecno):
        self.__tecno = tecno

    # Метод retail_price принимает аргумент для
    # розничной цены телефона
    def retail_price(self, price):
        self.__price = price

    # метод get_model_type возвращает тип модели телефона
    def get_model_type(self):
        return self.__model

    # метод get_tecno возвращает производителя телефона
    def get_tecno(self):
        return self.__tecno

    # метод get_retail_price возвращает розничную цену телефона
    def get_retail_price(self):
        return self.__price