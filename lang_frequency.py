from collections import Counter
import string
import os
import argparse


def load_data(file_path):
    if not os.path.exists(file_path):
        print('No such file in directory')
        return None
    else:
        with open(file_path) as file:
            text_file = file.read()
            return text_file


def delete_punctuation(text):
    punctuation_symbols = string.punctuation + '—«»'
    text_without_punctation = str.maketrans('', '', punctuation_symbols)
    return text.translate(text_without_punctation).split()


def get_most_frequent_words(list_of_words):
    counter = Counter(list_of_words)
    popular_words = counter.most_common()
    return popular_words


def show_word(popular_words):
    output_result_limit = 10
    for word in range(output_result_limit):
        print('{}. {} -> {}'.format(word + 1,
                                    popular_words[word][0],
                                    popular_words[word][1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File path')
    parser.add_argument('--path', type=str)
    args = parser.parse_args()
    file_with_text = load_data(args.path)
    text_without_punctation = delete_punctuation(file_with_text)
    show_word(get_most_frequent_words(text_without_punctation))

