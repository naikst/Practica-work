#Будет складывать числа(int, float) и строки(str) при Try и Except
def add_everything_up(a, b):
    # стандартная операция сложений
    try:
        result = a + b
        return result # Если сложение прошло успешно, возвращаем результат
    except TypeError:
            # Этот блок сработает, если в try возникнет TypeError
            # Проверяем, являются ли a и b объектами разных типов
            if isinstance(a, str) and isinstance(b, (int, float)) or \
                    isinstance(b, str) and isinstance(a, (int, float)):
                # Возвращаем строковое представление a и b, соединив вместе
                    return str(a) + str(b)
            else:
                 # Если причина TypeError другая, пробрасываем ошибку дальше
                 raise

#Пример кода:

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))