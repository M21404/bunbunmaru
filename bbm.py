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
        return 0
    else:
        print(f"{filename} already exists")
        return 1


def main(file, url):
    return writeToFile(url2string(url), file)


if __name__ == '__main__':
    # Example:
    # > py bbm.py sample.md https://www.newyorker.com/books/page-turner/thoreau-in-love
    file, url = sys.argv[1], sys.argv[2]
    exit_code = main(file, url)
    if exit_code == 0:
        print(f'Successfully wrote {url} to {file}')
