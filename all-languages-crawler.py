#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

lang_codes = set()
with open('language-codes.txt') as fin:
    for line in fin:
        lang_codes.add(line.strip())

for lang in lang_codes:
    print("\nCrawling: {}".format(lang.upper()))
    continue
    run = 'python3 wikipedia-crawler.py https://{0}.wikipedia.org/wiki/ --output={0}.txt --articles=100 --interval=1'.format(lang)
    os.system(run)

print("\nALL LANGUAGES DONE!")
