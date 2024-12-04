import mountain_Eagle  # Импортируем модуль mountain_Eagle для работы с классом Coin

def main():  # Основная функция, которая выполняет основное действие программы
    my_couns = mountain_Eagle.Coin()  # Создаем экземпляр класса Coin из модуля mountain_Eagle

    print(my_couns.get_sideup())  # Выводим текущую сторону монеты
    flip(my_couns)  # Подбрасываем монету, чтобы изменить состояние

    print(my_couns.get_sideup())  # Выводим новую сторону монеты после подбрасывания


def flip(coin):  # Функция, которая принимает объект coin и вызывает метод toss
    coin.toss()  # Изменяет состояние объекта coin, подбрасывая его


if __name__ == "__main__":  # Проверяем, запущен ли файл как основной модуль, и вызываем main
    main()