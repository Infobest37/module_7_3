
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    # Удаляем все символы пунктуации из строки
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    # Разбиваем строку на слова и добавляем в список
                    f_2 = line.lower().split()
                    words.extend(f_2)
                all_words[file] = words







        return all_words

    def find(self, word):
        # Делаем поиск по ранее сохраненным данным в self.all_words
        # Приводим искомое слово к нижнему регистру
        word = word.lower()
        result = {}
        for file, words in self.get_all_words().items():  # Используем self.all_words
            if word in words:
               result[file] = words.index(word.lower())+1 # Можно вернуть количество вхождений
               return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file, words in self.get_all_words().items():
            if word in words:
                result[file] = words.count(word.lower())
                return result









finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))