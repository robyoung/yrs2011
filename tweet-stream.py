from nltk.corpus import stopwords
from collections import defaultdict
from util import tokenize, tweets, tag_tweets
from review_text import load_all

def count_tokens(tokens, stops=None):
    stops = stops or []
    counts = defaultdict(int)
    for token in tokens:
        if token not in stops:
            counts[token] += 1
    return sorted((count, token) for token, count in counts.items())

def top_tokens(tokens):
    return [item for item in reversed(tokens[-10:])]

def unique_tokens(tokens):
    return [token for count, token in tokens if count == 1]

token_map = {}
for tweet in tweets():
    for token, tag in tag_tweets(tokenize(tweet['text'])):
        token_map.setdefault(tag, []).append(token)

for tag, tokens in token_map.items():
    print "% 10s % 8s % 6s" % (tag, len(tokens), len(set(tokens)))

print ""
print "EMOTICONS"
print "========="
counted = count_tokens(token_map['emoticon'])
print top_tokens(counted)
print len(unique_tokens(counted))
print ""

print "URLS"
print "===="
counted = count_tokens(token_map['url'])
print top_tokens(counted)
print len(unique_tokens(counted))
print ""

print "HASHTAGS"
print "========"
counted = count_tokens(token_map['#'])
print top_tokens(counted)
print len(unique_tokens(counted))
print ""

print "@REPLIES"
print "========"
counted = count_tokens(token_map['@'])
print top_tokens(counted)
print len(unique_tokens(counted))
print ""

print "WORDS"
print "====="
counted = count_tokens(token_map['word'], stopwords.words("english") + ["&", "it's"])
print top_tokens(counted)
print len(unique_tokens(counted))


review_tokens, review_docs = load_all("reviews")

review_tokens = set(token for token, count in review_tokens.items())
tweet_tokens = set(token for count, token in counted)

print "tweet tokens: %s" % len(tweet_tokens)
print "review tokens: %s" % len(review_tokens)
print len(tweet_tokens & review_tokens)
print len(tweet_tokens - review_tokens)
print len(review_tokens - tweet_tokens)
