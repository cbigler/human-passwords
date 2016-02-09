# -*- coding: utf-8 -*-
import importlib
import random
import string


def _randomword(dict, length):
   return random.choice(dict.d[length])


def _randomnumber(length):
   return ''.join(random.choice(string.digits) for i in range(length))


def generate(language='en'):
    dict = importlib.import_module('human_passwords.dictionary.{}'.format(language))
    return '{}{}{}{}'.format(_randomword(dict, 4), _randomnumber(4),
                             _randomword(dict, 5), _randomnumber(4))
