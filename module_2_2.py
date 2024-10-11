num = int(input("Введите любое число: "))
num_1 = int(input("Введите любое число: "))
num_2 = int(input("Введите любое число: "))
if num == num_1 and num_1 == num_2:
    print(3)
elif num == num_1 or num_1 == num_2 or num == num_1:
    print(2)
else:
    print(0)