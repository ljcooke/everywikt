@everywikt
==========

[@everywikt][] is a Twitter bot posting randomly selected words from
Wiktionary.

Requirements
------------

This script runs with Python 3 and depends on a separate module named
[botutil][].

It requires a file listing all of the article titles on Wiktionary:

 1. Go to http://dumps.wikimedia.org/enwiktionary/latest/ to see the latest
    archive of the English Wiktionary site.
 1. Download the file named _enwiktionary-latest-all-titles-in-ns0.gz_.
 1. Decompress the file using `gunzip`.
 1. Move the decompressed file to the _data_ directory.

Usage
-----

To print a single tweet on the command line, run:

    ./everywikt.py

To publish a tweet:

    export TWITTER_CONSUMER_KEY="appkey"
    export TWITTER_CONSUMER_SECRET="appsecret"
    export TWITTER_USER_TOKEN="123456789-mytoken"
    export TWITTER_USER_SECRET="mysecret"

    ./everywikt.py tweet

On the first run the script will take a short while to respond. Here it
generates an index of the Wiktionary file before preceding, so on subsequent
runs it will retrieve a random word very quickly.

[@everywikt]: https://twitter.com/everywikt
[botutil]: https://github.com/araile/python-botutil
