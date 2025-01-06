def all_variants(text):
    # Внешний цикл: перебираем длины подпоследовательностей
    for length in range(1, len(text) + 1):
        # Внутренний цикл: перебираем начальные позиции для текущей длины
        for i in range(len(text) - length + 1):
            # Возвращаем подстроку от i до i + length
            yield text[i:i + length]

# Пример использования
a = all_variants("abc")

# Выводим все подпоследовательности
for i in a:
    print(i)