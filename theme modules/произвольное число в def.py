# # def summator(txt, *values, type ='sum'):
# #     s = 0
# #     for i in values:
# #         s += i
# #
# #     return f"{txt}{s} {type}"
#
#
# # print(summator("Сумма чисел: ", 2, 3, 4, 5, type='summator'))
#
#
# def info(*value, **values):
#     for key, value in values.items():
#         print(key, value)
#
#
# info("Параметры по умолчанию ", name='Nikita', course='Python')


def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)


my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")