name = 'immutable_var'
name = (1, 'зима', 4.2,  True,)
print(name)
# name [0] = 200  причина ошибки появляется потому, что нельзя добавлять выше значений элемента кортежа.
# print(name)
name2 = 'immutable_var'
name2 = [5, 8, 9, 2]
print(name2)
name2 [0] = 4
print(name2)