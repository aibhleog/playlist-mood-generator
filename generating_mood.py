'''

Code to quickly generate a combination of 2 words to prompt Erini in 
making a playlist.  Bonus points if the resulting words are real weird.

Uses the wonderwords and wordhoard packages.


Stretch goal:
> allow inputs -- like "surprise me", "three words", word lengths, etc.
> app? or perhaps texting thing?

'''

import random_words as words # written by TAH

part1 = words.get_word('adjective')
part2 = words.get_word('noun')

print(f'Your playlist prompt is: {part1} {part2}')



# let's get more specific

part1 = words.get_word('adjective',kwargs={'word_min_length':5})
part2 = words.get_word('noun',kwargs={'word_min_length':6})

print(f'Your modified playlist prompt is: {part1} {part2}')


# let's have three words

part1 = words.get_word('adjective',kwargs={'word_min_length':3})
part1p5 = words.get_word('adjective',kwargs={'word_min_length':5})
part2 = words.get_word('noun',kwargs={'word_min_length':6})

print(f'Your 3-word playlist prompt is: {part1} {part1p5} {part2}')






