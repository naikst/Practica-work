## Эта программа расконсервирует объекты класса CellPhone.

import pickle  # Импортируем модуль pickle для работы с сериализованными данными.
import method_cellphone  # Импортируем модуль method_cellphone для работы с объектами телефонов.

FILENAME = 'cellphones.dat'  # Определяем имя файла, содержащего сериализованные данные.


def main():
    # Главная функция программы, которая выполняет чтение данных из файла
    end_of_file = False  # Инициализируем флаг окончания файла.

    input_file = open(FILENAME, 'rb')  # Открываем файл для чтения в двоичном режиме

    while not end_of_file:
        try:
            phone = pickle.load(input_file)  # Пытаемся загрузить следующий объект из файла.
            display_data(phone)  # Если объект успешно считан, выводим его данные.

            if isinstance(phone, method_cellphone.CellPhone):  # Проверьте, что объект phone
                # является экземпляром CellPhone
                display_data(phone)
        except EOFError:
            end_of_file = True  # Устанавливаем флаг, если достигли конца файла.

    input_file.close()  # Закрываем файл после завершения чтения данных.


def display_data(phone):
    # Функция для вывода данных о телефоне
    print(f"Manufacturer: {phone.ret_tecno()}")  # Выводим производителя телефона.
    print(f"Model: {phone.get_model_number()}")  # Выводим номер модели телефона.
    print(f"Retail Price: {phone.get_retail_price()}₽")  # Выводим розничную цену телефона.
    print()  # Печатаем пустую строку для разделения выводов.


if __name__ == "__main__":
    main()  # Запускаем выполнение программы
