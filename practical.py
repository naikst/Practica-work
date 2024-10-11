def convert(
        minutes):  # Функция принимает параметр minutes, который является целым числом, представляющим количество минут.

    return minutes * 60  # Для перевода минут в секунды нужно умножить количество минут на 60, так как в одной минуте
    # 60 секунд.


# Функция должна вернуть результат этого умножения.

print(convert(5))
print(convert(2))


def how_many_seconds(hours):
    return hours * 60 * 60  # переводим часы в секунды


print(how_many_seconds(2))
print(how_many_seconds(10))
print(how_many_seconds(24))