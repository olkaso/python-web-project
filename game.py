# -*- coding: utf-8 -*-
import random
from collections import Counter
import requests
from requests.exceptions import HTTPError


DICTIONARY_API_LINK = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang=ru-ru&text={}'
DICTIONARY_API_KEY = '' # your key goes here


def choose_source_words(amount):
    with open('dict.txt') as file:
        list_of_words = file.readlines()
    words = random.sample(list_of_words, amount)
    return words


def is_noun(word):
    response = requests.get(DICTIONARY_API_LINK.format(DICTIONARY_API_KEY, word))
    for i in range(5):
        response = requests.get(DICTIONARY_API_LINK.format(DICTIONARY_API_KEY, word))
        try:
            response.raise_for_status()
        except HTTPError as err:
            print('HTTP error occurred: '.format(err))
        except Exception as err:
            print('Other error occurred: {}'.format(err))
        else:
            break
    info = response.json()
    try:
        info = info['def'][0]['pos']
    except Exception:
        return False
    else:
        return info == 'noun'


class Game:
    def __init__(self):
        self._source_word = ""
        self._source_letters = Counter()
        self.guessed_words = []
        
    def is_part_of_source(self, word):
        letters = Counter(word)
        return len(list((self._source_letters & letters).elements())) == len(word)

    def set_source_word(self, word):
        self._source_word = word
        self._source_letters = Counter(self._source_word)

    def get_source_word(self):
        return self._source_word

    def get_message(self, word):
        word = word.lower()
        message = ""
        if not word.isalpha():
            message = 'Недопустимые символы'
        elif not self.is_part_of_source(word):
            message = "В слове есть буквы не из исходного"
        elif not is_noun(word):
            message = "Нет такого существительного"
        elif word in self.guessed_words:
            message = "Это слово уже было"
        else:
            self.guessed_words.append(word)
        return message
