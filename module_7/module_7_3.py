class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в атрибуте класса

    def get_all_words(self):
        all_words = {}  # Создаем пустой словарь для хранения результатов

        for file in self.file_names:  # Перебираем названия файлов
            with open(file, 'r', encoding='utf-8') as f:  # Открываем файл
                content = f.read().lower()  # Читаем содержимое файла и приводим к нижнему регистру
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:  # Убираем знаки препинания
                    content = content.replace(punct, ' ')  # Заменяем знаки препинания на пробелы
                words = content.split()  # Разбиваем текст на слова
                all_words[file] = words  # Сохраняем список слов в словарь с ключом - имя файла

        return all_words  # Возвращаем словарь со словами после обработки всех файлов

    def find(self, word):  # Метод для поиска слова
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}  # Создаем пустой словарь для хранения результатов

        for file_name, words in all_words.items():  # Перебираем все файлы и их слова
            if word in words:  # Проверяем, есть ли слово в списке слов
                position = words.index(word)  # Находим позицию первого вхождения слова
                result[file_name] = position + 1  # Сохраняем в словарь: имя файла и позицию слова

        return result  # Возвращаем словарь с результатами

    def count(self, word):  # Метод для подсчета количества вхождений слова
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        result = {}  # Создаем пустой словарь для хранения результатов

        for file_name, words in all_words.items():  # Перебираем все файлы и их слова
            count = words.count(word)  # Считаем количество вхождений слова в списке
            if count > 0:  # Если слово найдено
                result[file_name] = count  # Сохраняем в словарь: имя файла и количество вхождений

        return result  # Возвращаем словарь с результатами


# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Поиск позиции слова "TEXT"
print(finder2.count('teXT'))  # Подсчет вхождений слова "teXT"