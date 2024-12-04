
import time
import method_cellphone

# Главная функция программы
def main():
    # Создаем список телефонов, вызывая make_list
    phones = make_list()

    # Выводим данные о моделях телефонов
    print('Вывод запроса данных моделей: ')
    display_list(phones)

# Функция для создания списка телефонов
def make_list():
    # Создаем пустой список для хранения телефонов
    phone_list = []

    print("Введите данные о 5 телефонах.")
    # Цикл для ввода данных о пяти телефонах
    for i in range(1, 6):
        print(f'Номер телефона {i}')
        # Вводим название бренда телефона
        man = input('Введите название бренда: ')
        # Вводим номер модели телефона
        model = input('Введите номер модели: ')
        # Вводим розничную цену телефона и преобразуем в число с плавающей точкой
        retail = float(input('Розничная цена смартфона: '))
        print()

        # Создаем объект CellPhone с введенными данными
        phone = method_cellphone.CellPhone(man, model, retail)
        # Добавляем созданный объект в список телефонов
        phone_list.append(phone)

    # Возвращаем заполненный список телефонов
    return phone_list

# Функция для вывода списка телефонов
def display_list(phone_list):
    # Проходимся по каждому телефону в списке
    for item in phone_list:
        # Выводим бренд, номер модели и розничную цену
        print(item.ret_tecno(),
              item.get_model_number(),
              item.get_retail_price())
        print()

# Если файл запущен как основная программа, вызываем main
if __name__ == '__main__':
    main()
