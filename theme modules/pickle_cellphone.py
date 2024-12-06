import pickle  # Импортируем модуль pickle для сериализации объектов.
import method_cellphone  # Импортируем модуль method_cellphone, в котором описан класс CellPhone.

FILENAME = 'cellphones.dat'  # Константа, хранящая название файла для сохранения данных о телефонах.

def main():
    # Главная функция программы, отвечает за ввод данных и их сохранение в файл.
    again = 'д'  # Переменная, контролирующая цикл повторного ввода данных.

    output_file =  open(FILENAME, 'wb')

    while again.lower() == 'д':  # Цикл, продолжающийся пока пользователь желает вводить данные.
        manuf = input('Введите производителя: ')  # Ввод производителя телефона.
        model = input('Введите модель: ')  # Ввод модели телефона.
        price = float(input('Введите цену: '))  # Ввод цены телефона, преобразуем в тип float.

        cell_phone = method_cellphone.CellPhone(manuf, model, price)  # Создаем объект CellPhone с введёнными данными.

        pickle.dump(cell_phone, output_file)  # Сохраняем объект cell_phone в файл output_file.

        again = input('Продолжить ввод? (д/н): ')  # Спрашиваем пользователя, хочет ли он продолжить ввод данных.

    output_file.close()  # Закрываем файл после завершения ввода данных.
    print(f'Сохранение завершено в {FILENAME}.')


if __name__ == '__main__':  # Проверяем, была ли программа запущена напрямую.
    main()
    output_file = open(FILENAME, 'wb')  # Открываем файл для записи в бинарном режиме.