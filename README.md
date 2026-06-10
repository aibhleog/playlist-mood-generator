# Playlist Mood Generator

This repo randomly generates a playlist mood, from 1+ adjectives and a noun.  To make it more fun, it takes each randomly-generated word and then searches for synonyms, then randomly chooses a new word from the list of synonyms+original word.

Yes, definitely overkill.  Sue me. 🔪

### examples

```
[1] run generating_mood.py
Your playlist prompt is: gamey draw
Your modified playlist prompt is: juicy risk capital
Your 3-word playlist prompt is: conscientious semiliterate nominee

[2] run generating_mood.py
Your playlist prompt is: royal communicator
Your modified playlist prompt is: aerial bone
Your 3-word playlist prompt is: misanthropical beamish reservation

[3] run generating_mood.py
Your playlist prompt is: unthoughtful forelimb
Your modified playlist prompt is: permanent azimuth
Your 3-word playlist prompt is: never-ending tenor refracting telescope
```


-----------

### where Taylor left off

I wanted to find a way to make this a little app that you could SMS text to get your daily mood prompt (to build your playlist).  I started looking into Twilio, which has a free 30-day trial.  SMS texting FROM the free trial account worked, but it was getting complicated trying to figure out how to go the other direction.  In a perfect world, one would be able to text for the mood prompt AND be able to add specifications.

However at that point, perhaps it should just be a small app?  Regardless, I stopped for now.  We'll see if I get back to the SMS part before my free Twilio trail runs out.
