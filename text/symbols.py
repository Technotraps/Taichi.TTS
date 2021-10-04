""" Из https://github.com/keithito/tacotron """

'''
Определяет набор символов, используемых при вводе текста в модель.

По умолчанию используется набор символов ASCII, который хорошо подходит для английского языка или текста, прошедшего через Unidecode. Для других данных вы можете изменить _characters. Подробности см. в TRAINING_DATA.md. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Добавляйте "@" к символам ARPAbet для обеспечения уникальности (некоторые из них совпадают с прописными буквами):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Экспорт всех символов:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
