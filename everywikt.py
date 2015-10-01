#!/usr/bin/env python3
import sys
from random import choice, randint
from urllib.parse import quote

from botutil import BigList, post_tweet

WIKT_FILENAME = 'data/enwiktionary-latest-all-titles-in-ns0'
SYMBOL_FILENAME = 'data/symbols.txt'

LINK_LEN = 23
MAX_SYMBOL_LEN = 1
MAX_WORD_LEN = 140 - LINK_LEN - MAX_SYMBOL_LEN - 2

def format_tweet(word, symbol):
    assert ' ' not in word
    link = 'https://en.wiktionary.org/wiki/' + quote(word.encode('utf-8'))
    word = word.replace('_', ' ')
    assert 0 < len(symbol) <= MAX_SYMBOL_LEN
    return ' '.join((word, symbol, link))

def generate_tweet():
    words = BigList(WIKT_FILENAME)
    symbol = BigList(SYMBOL_FILENAME).choice().strip()
    for _ in range(10):
        word = words.choice(start=1).strip()
        if len(word) <= MAX_WORD_LEN:
            return format_tweet(word, symbol)

def main():
    tweet = generate_tweet()
    if not tweet:
        sys.stderr.write('Could not generate a tweet in 140 characters!\n')
        return 1

    if 'tweet' in sys.argv:
        post_tweet(tweet)
    else:
        print(tweet)

if __name__ == '__main__':
    sys.exit(main())
