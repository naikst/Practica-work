salary = [2300, 1800, 5000, 3456.90, 5800.23]
print(round(sum(salary)/len(salary), 1), "- Среднаяя зарплата в компаний")
print(round(max(salary), 2), "- Максимальная зарплата в компаний")
print(round(min(salary), 3), "- Минимальное зарплата в компаний")

names = ["Женя", "Антон", "Егор", "Катя", "Саша"]
zipped = dict(zip(names, salary))
print(zipped['Антон'], "- Зарплата Антона")

#int() - целое число
#float() - число с плавающей запятой
#bool() - логические значения
#str() - строки
#list() - список
#tuple() - кортеж
#dict() - словарь
#set() - множество


# Максимум в списке

def fin_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


print(fin_max([42345, 345346, 123124, 4356456]))


# Подсчета четный числе в списке

def count_max(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter


print(fin_max([2, 3, 4, 5, 6, 1, 0]))


# Уникальный список

def unicue(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
                new_list.append(i)

        return new_list

print(unicue([1, 3, 4, 5, 6, 7, 234, 78, 2934]))
