import sys
import time
import os
import requests
from readability import Document
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def url2string(url, toc=False):
    response = requests.get(url)
    doc = Document(response.text)
    title = doc.title()
    content = md(doc.summary())
    return f"""+++
title = "{title}"
date = "{time.strftime("%Y-%m-%d")}"
TableOfContents = "{toc}"
draft = false
source = "{url}"
+++
{content}
"""


def writeToFile(content, filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(content)
    else:
        print(f"{filename} already exists")


def main(file, url):
    writeToFile(url2string(url), file)


if __name__ == '__main__':
    # Example:
    # > py bbm.py sample.md https://www.newyorker.com/books/page-turner/thoreau-in-love
    file, url = sys.argv[1], sys.argv[2]
    main(file, url)
    print(f'Successfully wrote {url} to {file}')
