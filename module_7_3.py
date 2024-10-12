class WordsFinder:
    def __init__(self, *file_names):
        # *file_names означает, что мы можем передать любое количество файлов
        self.file_names = file_names  # Создаём список файлов

    def get_all_words(self):
        # Возвращает список слов
        all_words = {}
        # Перебираем все файлы
        for file_name in self.file_names:
            # Получаем список слов из каждого файла
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()  # Читаем содержимое файла и приводим к нижнему регистру
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:  # Убираем знаки препинания
                    content = content.replace(punct, ' ')

                words = content.split()  # Разбиваем строку на список слов
                all_words[file_name] = words  # Сохраняем список слов в словарь с ключом - имя файла

        return all_words

    def find(self, word):  # Возвращает позицию слова в тексте
        word = word.lower()  # Приводим к нижнему регистру
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word_positions = {}
        for file_name, words in all_words.items():
            try:
                # Ищем индекс первого вхождения слова
                position = words.index(word) + 1  # Получаем позицию в списке слов, начинаем с 1
                word_positions[file_name] = position
            except ValueError:
                # Если слово не найдено, пропускаем файл
                continue

        return word_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()  # Получаем все слова из файлов
        word_counts = {}

        for file_name, words in all_words.items():  # Проходим по файлам
            count = words.count(word)  # Подсчитываем количество вхождений слова в списке слов
            if count > 0:
                word_counts[file_name] = count  # Добавляем в словарь, если слово найдено

        return word_counts


# Пример использования:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Поиск позиции слова "TEXT"
print(finder2.count('teXT'))  # Подсчет вхождений слова "teXT"