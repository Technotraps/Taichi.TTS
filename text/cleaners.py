""" from https://github.com/keithito/tacotron """

'''
Очистители - это преобразования, которые выполняются над входным текстом как во время обучения, так и во время оценки.
Очистители могут быть выбраны путем передачи списка имен очистителей через запятую в качестве гиперпараметра "cleaners".
гиперпараметр. Некоторые очистители специфичны для английского языка. Как правило, вы захотите использовать:
  1. "english_cleaners" для английского текста
  2. "russian_cleaners" для русского текста
  2. "transliteration_cleaners" для неанглийского текста, который может быть транслитерирован в ASCII с помощью библиотеки Unidecode ().
     библиотеки Unidecode (https://pypi.python.org/pypi/Unidecode).
  3. "basic_cleaners", если вы не хотите транслитерировать (в этом случае вы также должны обновить
     символы в symbols.py, чтобы они соответствовали вашим данным).

Переведено с помощью www.DeepL.com/Translator (бесплатная версия)
'''

import re
from unidecode import unidecode
from .numbers import normalize_numbers

# Регулярное выражение, сопоставляющее пробелы:
_whitespace_re = re.compile(r'\s+')

# Список пар (регулярное выражение, замена) для аббревиатур:
_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
  ('mrs', 'misess'),
  ('mr', 'mister'),
  ('dr', 'doctor'),
  ('st', 'saint'),
  ('co', 'company'),
  ('jr', 'junior'),
  ('maj', 'major'),
  ('gen', 'general'),
  ('drs', 'doctors'),
  ('rev', 'reverend'),
  ('lt', 'lieutenant'),
  ('hon', 'honorable'),
  ('sgt', 'sergeant'),
  ('capt', 'captain'),
  ('esq', 'esquire'),
  ('ltd', 'limited'),
  ('col', 'colonel'),
  ('ft', 'fort'),
]]


def expand_abbreviations(text):
  for regex, replacement in _abbreviations:
    text = re.sub(regex, replacement, text)
  return text


def expand_numbers(text):
  return normalize_numbers(text)


def lowercase(text):
  return text.lower()


def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)


def convert_to_ascii(text):
  return unidecode(text)


def basic_cleaners(text):
  '''Basic pipeline that lowercases and collapses whitespace without transliteration.'''
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def transliteration_cleaners(text):
  '''Pipeline for non-English text that transliterates to ASCII.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text


def english_cleaners(text):
  '''Pipeline for English text, including number and abbreviation expansion.'''
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = expand_numbers(text)
  text = expand_abbreviations(text)
  text = collapse_whitespace(text)
  return text
def russian_cleaners(text):
  text = convert_to_ascii(text)
  text = lowercase(text)
  # к сожалению мне не удалось найти библиотеку для перевода чисел в слова
  text = collapse_whitespace(text)
