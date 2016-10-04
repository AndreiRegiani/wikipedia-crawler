# wikipedia-crawler
Extracts plain-text from series of Wikipedia articles and saves to a local text file.

The goal is to have text samples of a specific language on a specific topic, that can be used on computer analysis applied to linguistics (word frequency, distribution, etc), **or to generate wordlists of any language on Wikipedia (294 in total)**.

## Usage:

    python3 wikipedia-crawler.py https://en.wikipedia.org/wiki/Biology

Creates `output.txt`, extracting only this unique article.

    python3 wikipedia-crawler.py https://en.wikipedia.org/wiki/Biology --articles=10 --interval=5 --output=biology.txt

Creates `biology.txt`, crawling `10` articles related to `Biology`. Requests interval set to `5` seconds (default).
Session log containing all visited URLs is saved as `session_biology.txt`.

If the initial article is [Biology](https://en.wikipedia.org/wiki/Biology), the crawler will continue on related pages like [Natural Science](https://en.wikipedia.org/wiki/Natural_science), [Organisms](https://en.wikipedia.org/wiki/Organims), [Evolution](https://en.wikipedia.org/wiki/Evolution), ...

## Dependencies:
* [BeautifulSoap 4](https://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/)

`pip install beautifulsoup4`
`pip install requests`
