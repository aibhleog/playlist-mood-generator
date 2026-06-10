'''

Testing integration from python to Twilio to text.


CURRENT STATUS:
----------------
I made a free 30-day trial account with Twilio (10July2026)
and connected it to my google phone #.

Got stuck trying to figure out how to use text 
prompts to run the code. Too many needs.


'''

import random_words as words # written by TAH
from twilio.rest import Client
from twilio_account_info import *
import sys

# this is the trial account info, with texts sent to my google phone #
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
twilio_number = TWILIO_NUMBER
recipient_number = RECIPIENT_NUMBER


sys.exit(0)

# Create Twilio client
client = Client(account_sid, auth_token)


# getting playlist prompt
part1 = words.get_word('adjective',kwargs={'word_min_length':5})
part2 = words.get_word('noun',kwargs={'word_min_length':6})
message = f'''

This is your playlist mood:

{part1} {part2}

'''


# Send SMS
# in body part you have to write your message
message = client.messages.create(
    body=message,
    from_=twilio_number,
    to=recipient_number
)

print(f"Message sent with SID: {message.sid}")