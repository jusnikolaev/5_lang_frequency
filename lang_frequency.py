import requests
from collections import Counter
import string


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        file = str(file.read().lower())
        a = string.punctuation + '—«»'
        print(a)
        print(string.punctuation)
        translator = str.maketrans('', '', a)
        return file.translate(translator).split()


def get_most_frequent_words(text):
    counter = Counter(text)
    print('Самые популярные слова:')
    for item_number, item in enumerate(counter.most_common()):
        popular_words = counter.most_common()[item_number]
        print('{} -> {}'.format(popular_words[0],
                                popular_words[1]))


if __name__ == '__main__':
    text_file = load_data('text.txt')
    get_most_frequent_words(text_file)
