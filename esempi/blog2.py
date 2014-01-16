#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html
import pprint
import sys

URL = "http://googleblog.blogspot.it"

html = requests.get(URL).content
dom = lxml.html.fromstring(html)

for entry in dom.cssselect('.post'):
    post = {
        'title': entry.cssselect('h2.title')[0].text_content(),
        'date': entry.cssselect('.publishdate')[0].text_content(),
        'url': entry.cssselect('h2 a')[0].get('href'),
    }
    pprint.pprint(post)

    scraperwiki.sql.save(['url'], post)
