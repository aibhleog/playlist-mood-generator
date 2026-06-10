'''

Using a word generator as input into a synonym generator.
Limiting to thesaurus.com for searching so it runs faster.

'''
import wordhoard as wo
import wonderwords as ww
import numpy as np
import sys
import os, contextlib


def get_word(category,verbose=False,kwargs={}):
    '''
    Returns a random word based upon syntax category
    -------------------------------------------------
    If wanting output, set verbose to True.  Also included an
    empty kwargs dictionary in case you want more criteria for the
    initial random word.
    
    '''
    input_word = ww.RandomWord().word(include_categories=[category],
                                      exclude_with_spaces=True,**kwargs)
    if verbose == True: print(f'For input {input_word}... the word is ',end='')
    
    # running through the with's so if it fails on first try, 
    # it suppresses the fail statement 
    with open(os.devnull, 'w') as devnull:
        with contextlib.redirect_stdout(devnull):
            # getting synonyms
            synonyms = wo.Synonyms(search_string=input_word,sources=['thesaurus.com']).find_synonyms()
            # if none from thesaurus.com, tries synonym.com
            if type(synonyms) == type(None):
                synonyms = wo.Synonyms(search_string=input_word,sources=['synonym.com']).find_synonyms()
                if type(synonyms) == type(None): 
                    return input_word # word may be too specific, just returns original word :)
            
    # adding original word into list to keep as an option
    synonyms = np.concatenate((synonyms,[input_word]))
    
    # random number from list of length synonyms
    num = np.random.randint(low=0,high=len(synonyms))
    word = synonyms[num] # the final word
    if verbose == True: print(word)
    
    return word

