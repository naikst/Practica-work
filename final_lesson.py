grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_list = sorted(students)
avg_grades = {}
for i in range(len(sorted_list)):
    avg_grades[sorted_list[i]] = sum(grades[i]) / len(grades[i])
print(avg_grades)