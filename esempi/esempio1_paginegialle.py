import requests
URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"

from os.path import exists

if not exists('pizzerie.html'):
    data = requests.get(URL)
    html = data.content
    open('pizzerie.html','w').write(html)
else:
    html = open('pizzerie.html','r').read()


import re
links = re.findall(r'\<a.*\</a',html)

clinks = filter(lambda x: re.search(r'class="_lms _noc"',x), links)

pizzerie_1 = map(lambda x: re.sub(r'^.*title="Scheda Azienda ([^"]+)".*$','\\1',x), clinks)

