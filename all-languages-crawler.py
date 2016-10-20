#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple utility that uses 'wikipedia-crawler.py' to get plain-text articles 
from 269 languages (language-codes.txt)
"""

import os

ARTICLES = 10
INTERVAL = 1.5

lang_codes = set()
with open('language-codes.txt') as fin:
    for line in fin:
        lang_codes.add(line.strip())

for lang in lang_codes:
    print("\nCrawling: {}".format(lang.upper()))
    run = 'python3 wikipedia-crawler.py https://{0}.wikipedia.org/wiki/Special:Random --output={0}.txt --articles={1} --interval={2}'.format(lang, ARTICLES, INTERVAL)
    os.system(run)

print("\nALL LANGUAGES DONE!")
