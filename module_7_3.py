import io
import string

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for name in self.file_names:

            with open(name, encoding='utf-8') as file:
                list_words = []
                for line in file:
                    line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                    list_words.extend(line.split())
                    all_words[name] = list_words

        return all_words

    def find(self, word):
        result = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                result[key] = value.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            result[value] = words_count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
            
finder1 = WordsFinder('Mother Goose.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

