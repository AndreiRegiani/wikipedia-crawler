# wikipedia-crawler
Extracts plain text from Wikipedia articles and saves to a local text file.

The goal is to have samples of a specific language on a specific topic, to be used on computer analysis applied to linguistics.
If the starting article is [Biology](https://en.wikipedia.org/wiki/Biology), the crawler will continue on related pages like [Natural Science](https://en.wikipedia.org/wiki/Natural_science), [Organisms](https://en.wikipedia.org/wiki/Organims), [Evolution](https://en.wikipedia.org/wiki/Evolution).

## Usage:
```python3 wikipedia-crawler.py https://en.wikipedia.org/wiki/Biology```

Creates `output.txt`, without crawling to other articles.

```python3 wikipedia-crawler.py https://en.wikipedia.org/wiki/Biology --articles=50 --interval=5 --output=articles.txt```

Creates `articles.txt`, crawling 50 articles related to Biology. Interval between requests set to 5 seconds (default).

## Dependencies:

* [BeautifulSoap 4](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/)
