grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразование в список
students_list = list(students)

# # Создание словаря для хранения среднего балла
averages_grades = {}

# Вычисление среднего балла для каждого студента
for i in range(len(students_list)):
    total = sum(grades[i])
    average = total / len(grades[i])  # средний балл
    averages_grades[students_list[i]] = average

print(averages_grades)
