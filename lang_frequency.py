from collections import Counter
import string
import os
import argparse


def valiate_path(file_path):
    if not os.path.exists(file_path):
        print('No such file in directory')
        return False
    else:
        return True


def load_data(file_path):
    with open(file_path) as file:
        text_file = file.read()
        return text_file


def delete_punctuation(text):
    punctuation_symbols = string.punctuation + '—«»'
    text_without_punctation = str.maketrans('', '', punctuation_symbols)
    return text.translate(text_without_punctation).split()


def get_most_frequent_words(list_of_words, limit_of_words):
    counter = Counter(list_of_words)
    popular_words = counter.most_common()
    return popular_words[0:limit_of_words]


def show_word(popular_words):
    for word in popular_words:
        print(word)
        print('{} -> {}'.format(word[0], word[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    if valiate_path(args.path):
        file_with_text = load_data(args.path)
        text_without_punctation = delete_punctuation(file_with_text)
        show_word(get_most_frequent_words(text_without_punctation, 9))

