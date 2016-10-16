#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

lang_codes = set()
with open('language-codes.txt') as fin:
    for line in fin:
        lang_codes.add(line.strip())

for lang in lang_codes:
    print("\nCrawling: {}".format(lang.upper()))
    run = 'python3 wikipedia-crawler.py https://{0}.wikipedia.org/wiki/ --output={0}.txt --articles=5 --interval=3'.format(lang)
    os.system(run)

print("\nALL LANGUAGES DONE!")
