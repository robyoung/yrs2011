from collections import defaultdict
import json
import os
from nltk.tokenize import WhitespaceTokenizer

def tokenize(message):
    return WhitespaceTokenizer().tokenize(message.lower())

def read(name, sentiment):
    path = os.path.join("data", name, sentiment)

    for filename in os.listdir(path):
        yield (filename, open(os.path.join(path, filename)).read())

def load(name, sentiment, tokens, docs):
    for name, text in read(name, sentiment):
        doc_tokens = tokenize(text)
        for token in doc_tokens:
            docs[name][token] += 1
        for token in set(doc_tokens):
            tokens[token] += 1
    return tokens, docs


def load_all(name):
    tokens = defaultdict(int)
    docs = defaultdict(lambda: defaultdict(int))

    load(name, "pos", tokens, docs)
    load(name, "neg", tokens, docs)

    return tokens, docs

def tweets():
    with open(os.join("data", "twitter-stream.json")) as f:
        for line in f:
            yield json.loads(line)

def tag_tweets(tokens):
    for token in tokens:
        if token.startswith("@"):
            yield (token, "@")
        elif token.startswith("#"):
            yield (token, "#")
        elif token.startswith("http://"):
            yield (token, "url")
        elif token[0] in ":;8" and token[-1] in "()D][{}pP3":
            yield (token, "emoticon")
        else:
            yield (token, "word")
