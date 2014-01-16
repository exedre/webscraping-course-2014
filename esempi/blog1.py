import scraperwiki
import requests
import lxml.html
import pprint
import sys

URL = sys.argv[1]

html = requests.get(URL).content
dom = lxml.html.fromstring(html)

for entry in dom.cssselect('.article'):
    post = {
        'title': entry.cssselect('h1 a')[0].text_content(),
        'date': entry.cssselect('.time')[0].text_content(),
        'url': entry.cssselect('h1 a')[0].get('href'),
    }
    pprint.pprint(post)

    scraperwiki.sql.save(['url'], post)



