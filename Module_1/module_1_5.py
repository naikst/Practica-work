# переменные разных типов данных
immutable_var = (1, 'зима', 4.2, True,)
print(immutable_var)

#  immutable_var [0] = 200  причина ошибки появляется потому, что нельзя добавлять выше значений элемента кортежа.
# print(immutable_var)


#Создание изменяемых структур данных
mutable_var = ([234], ['course', 4.23, False], [12, 34, 56, 78])
print(mutable_var)

mutable_var[0].append(123)
print(mutable_var)
