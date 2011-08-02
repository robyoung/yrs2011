import os
from util import tweets, tokenize, tag_tweets

def extract_emoticon(text):
    emoticons = []
    for token, tag in tag_tweets(tokenize(text)):
        if tag == "emoticon":
            emoticons.append(token)
#            text = text.replace(token, "")
    return emoticons, text

def get_mood(emoticons):
    pos = 0
    for emoticon in emoticons:
        if emoticon[-1] in "]})DpP":
            pos += 1
        else:
            pos -= 1
    return pos

for tweet in tweets():
    emoticons, text = extract_emoticon(tweet['text'])
    if emoticons:
        mood = get_mood(emoticons)
        print emoticons, mood
        if mood:
            with open(os.path.join("tweets", "pos" if mood > 0 else "neg", tweet['id_str']), "w+") as w:
                w.write(text.encode("utf-8", "ignore"))