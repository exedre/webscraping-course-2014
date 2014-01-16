import sys
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = sys.argv[1]
# url = 'http://www.repubblica.it'
br = mechanize.Browser()

urls = set()
visited = set()
errors = set()

urls.add(url)

while len(urls)>0:
    this = urls.pop()
    print this
    try:
        br.open(this)
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url)
            if url in newurl and newurl not in visited:
                urls.add(newurl)
        visited.add(this)
    except:
        errors.add(this)
        #if len(visited) % 1 == 0:
    print "E",len(errors),"U",len(urls),"V",len(visited)

open('links.txt','w').write('\n'.join(visited))
open('errors.txt','w').write('\n'.join(errors))

