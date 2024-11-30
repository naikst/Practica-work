#Работа со словарями
my_dict = {'Nikita': 1995, 'Sergey': 1996, 'Ivan': 1997}
print(f'Dict: {my_dict}')
# Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(f'Existing value: {my_dict["Sergey"]}')
print(f'Not existing value: {my_dict.get("Sofia")}')
# ещё две произвольные пары того же формата в словарь my_dict
my_dict.update({'Svetlana': 1994, 'Andrei': 1998})
print(my_dict)
del my_dict['Sergey']  # удаление одну из пар
print(my_dict) # Выведите на экран словарь my_dict.


#Работа с множествами
my_set = {3, 4, 4, 5, 23, 23}
print(f"Set: {my_set}")
my_set.add(55)
my_set.add(43)
my_set.remove(23)
print(f'Modified set: {my_set}')