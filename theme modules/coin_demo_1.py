# Эта программа импортирует имитационный модуль
# и создает три экземпляра класса Coin.
import  time
import mountain_Eagle

def main():
    # Создает три объекта класса Coin
    coin1 = mountain_Eagle.Coin()
    coin2 = mountain_Eagle.Coin()
    coin3 = mountain_Eagle.Coin()

    # Показать повернутую вверх сторону каждой монеты.
    print('Тут первоначальные сторон трех монет обращены вверх: ')
    print(coin1.get_sideup(),
          coin2.get_sideup(),
          coin3.get_sideup(), sep='\n')
    print()
    time.sleep(1)

    # Подбросить монету
    print('Сейчас буду подбрасывать все монеты которые имеется...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()
    time.sleep(3)


    # Показать повернутую вверх сторону каждой монеты после каждого подброса.
    print('Теперь стороны трех монет обращены вверх: ')
    print(coin1.get_sideup(),
          coin2.get_sideup(),
          coin3.get_sideup(), sep='\n')
    print()


    # Вызвать главную функцию
if __name__ == '__main__':
    main()

