from collections import Counter
import string
import os
import argparse


def load_data(file_path):
    if not os.path.exists(file_path):
        return False
    with open(file_path) as file:
        text = file.read()
        return text


def delete_punctuation(text):
    punctuation_symbols = string.punctuation + '—«»'
    clear_text = str.maketrans('','', punctuation_symbols)
    return text.translate(clear_text).split()


def get_most_frequent_words(list_of_words):
    print(list_of_words)
    counter = Counter(list_of_words)
    popular_words = counter.most_common()
    return popular_words


def show_word(popular_words):
    for word in range(10):
        print('{} -> {}'.format(popular_words[word][0], popular_words[word][1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    original_file_path = load_data(args.path)
    if original_file_path:
        clear_text = delete_punctuation(original_file_path)
        show_word(get_most_frequent_words(clear_text))
    else:
        print('Can\'t find file')

