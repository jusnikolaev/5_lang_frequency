from collections import Counter
import string
import argparse


# Загрузка файла
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as text_file:
        text_file = str(text_file.read().lower())
        a = string.punctuation + '—«»'
        translator = str.maketrans('', '', a)
        return text_file.translate(translator).split()


# Счетчик слов
def get_most_frequent_words(text):
    counter = Counter(text)
    print('Самые популярные слова:')
    for item_number, item in enumerate(counter.most_common()):
        popular_words = counter.most_common()[item_number]
        print('{} -> {}'.format(popular_words[0],
                                popular_words[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    text_file = load_data(args.path)
    if text_file:
        get_most_frequent_words(text_file)
    else:
        print('Can\'t find file')

