
# Предположим, что ret_tecno() должен возвращать название бренда
# Класс CellPhone представляет информацию о мобильном телефоне
class CellPhone:
    def __init__(self, manufacturer, model_number, retail_price):
        # Конструктор создает объект мобильного телефона
        # manufacturer - производитель телефона
        # model_number - номер модели телефона
        # retail_price - розничная цена телефона
        self.__manufacturer = manufacturer
        self.__model_number = model_number
        self.__retail_price = retail_price

    def ret_tecno(self):
        # Метод возвращает название производителя (бренда) телефона
        return self.__manufacturer

    def get_model_number(self):
        # Метод возвращает номер модели телефона
        return self.__model_number

    def get_retail_price(self):
        # Метод возвращает розничную цену телефона
        return self.__retail_price