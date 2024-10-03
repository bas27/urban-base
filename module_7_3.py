class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        ex = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words_dict = {}
        for file_name in self.file_names:
            words_list = []
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                for token in ex:
                    content = content.replace(token, ' ')
                for line in content.split():
                    for word in line.split():
                        words_list.append(word.lower())

            all_words_dict[file_name] = words_list
        return all_words_dict

    def find(self, word):
        finder = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                finder[name] = words.index(word.lower()) + 1
        return finder

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_dict[name] = words.count(word.lower())
        return count_dict


finder1 = WordsFinder('for_module_7_3/Walt Whitman - O Captain! My Captain!.txt',
                      'for_module_7_3/Rudyard Kipling - If.txt',
                      'for_module_7_3/Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
