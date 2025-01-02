# Исходные списки строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

#Длины строк из first_strings, если длина ≥ 5
first_result = [len(word) for word in first_strings if len(word) >= 5]

#Пары слов из first_strings и second_strings с одинаковой длиной
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

#Словарь {слово: длина} для слов с чётной длиной из объединенного списка
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print("first_result:", first_result)
print("second_result:", second_result)
print("third_result:", third_result)