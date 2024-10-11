def single_root_words(root_word, *other_words):
    #Приводим root_word к нижнему регистру для корректного сравнения
    root_word = root_word.lower()

    #Создаем пустой список для результата
    same_words = []

    #Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержит ли текущее слово root_word или наоборот
        if root_word in word_lower or word_lower in root_word:
            #Если условия выполняется, добавляем слово в результат
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


#Примеры вызова функций
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'riches')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

#Выводим результаты на экран
print(result1)
print(result2)
