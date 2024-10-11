import tkinter as tk  # Добавления библиотеки для удобства ввели обращения по имени 'tk'


def get_values():
    num1 = int(number1_entry.get())  # вытаскиваем в числа
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)
    insert_values(res)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    answer_entry.delete(0, "end")  # Удаляет предыдуший элемент  в "Ответ"
    answer_entry.insert(0, res)  # добвляет элемент в итог "Ответ"


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    answer_entry.delete(0, "end")  # Удаляет предыдуший элемент  в "Ответ"
    answer_entry.insert(0, res)  # добвляет элемент в итог "Ответ"


def div():
    num1, num2 = get_values()
    res = num1 / num2
    answer_entry.delete(0, "end")  # Удаляет предыдуший элемент  в "Ответ"
    answer_entry.insert(0, res)  # добвляет элемент в итог "Ответ"


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    answer_entry.delete(0, "end")  # Удаляет предыдуший элемент  в "Ответ"
    answer_entry.insert(0, res)  # добвляет элемент в итог "Ответ"


# Создаем окно
window = tk.Tk()  # переменная для создания класса
window.title('Калькулятор')  # Поменяли название нашей программы
window.geometry('350x350')  # Запрос на размер окна.
window.resizable(False, False)  # Делаем ограниченного размера окна и не доступна для изменений.
# Кнопки операций
button_add = tk.Button(window, text='+', width=2, height=2,
                       command=add)  # переменная хранящего  наш виджет в виде кнопки   I
button_add.place(x=100, y=200)  # Позволяет размещать элемент по кординатам II
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)  # I
button_sub.place(x=150, y=200)  # Размещение по кординатам. II
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)  # I
button_mul.place(x=200, y=200)  # II
button_div = tk.Button(window, text='/', width=2, height=2, command=div)  # I
button_div.place(x=250, y=200)  # II
# Поля для ввода и вывода данных
number1_entry = tk.Entry(window, width=28)  # Текстовое поле для введения Пользователя
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)  # Текстовое поле для введения Пользователя
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)  # Текстовое поле вывода(то есть итог после сложения)
answer_entry.place(x=100, y=300)
# Метки
number1 = tk.Label(window, text='Введите первое число:')  # Виджет для надписи IV
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число:')  # IV
number2.place(x=100, y=125)
answer = tk.Label(window, text='Ответ:')  # IV
answer.place(x=100, y=275)
# Запуск главного цикла
window.mainloop()  # Обновления событий
