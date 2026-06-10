'''

Exploring wonderwords package.
https://pypi.org/project/wonderwords/


'''
import wonderwords as ww
import numpy as np


r = ww.RandomWord()

# generate a random word
print(r.word())

# random word that starts with a and ends with en
print(r.word(starts_with="a", ends_with="en"))

# generate a random noun or adjective, by default all parts of speech are included
print(r.word(include_parts_of_speech=["nouns", "adjectives"]))

# generate a random word between the length of 3 and 8 characters
print(r.word(word_min_length=3, word_max_length=8))

# generate a random word with a custom regular expression
print(r.word(regex=".*a"))

# you can combine multiple filtering options
print(r.word(starts_with="ru", word_max_length=10, include_parts_of_speech=["verbs"]))


# get a list of ALL words that start with "am"
print(r.filter(starts_with="am"))

# you can use all the options found in the word method:
print(r.filter(ends_with="k", include_parts_of_speech=["verbs"], word_min_length=4))


# get a list of 3 random nouns
print(r.random_words(3, include_parts_of_speech=["nouns"]))

# you can use all the options found in the word method
print(r.random_words(5, starts_with="o", word_min_length=10))

# # if the amount of words you want to get is larger than the amount of words
# # there are, a NoWordsToChooseFrom exception is raised:
# print(r.random_words(100, starts_with="n", word_min_length=16))
# # there are less than 100 words that are at least 16 letters long and start with
# # n, so an exception is raised

# you can silence the NoWordsToChooseFrom exception and return all words even
# if there are less, by setting return_less_if_necessary to True
print(r.random_words(100, starts_with="n", word_min_length=16, return_less_if_necessary=True))






