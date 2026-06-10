'''

Exploring wordhoard package.
https://wordhoard.readthedocs.io/en/latest/


classes:
> Antonyms, Definitions, Hypernyms, Hyponyms and Synonyms


'''
import wordhoard as wo
import numpy as np


adjective = 'happy'


# running through the classes available
# NOTE: this takes a lonnnnggggg time...
for classit in [wo.Antonyms,wo.Synonyms,wo.Hypernyms,
                wo.Hyponyms,wo.Definitions]:
    obj = classit(search_string=adjective)
    obj_name = classit.__name__.lower()

    # getting words
    print(f'Getting {obj_name} for "{adjective}"...',end='\n\n')
    words = eval(f'obj.find_{obj_name}()')
    print(np.array(words),end='\n\n')
    