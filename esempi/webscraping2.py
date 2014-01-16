
from webscraping import download, xpath

engine = download.Download()

URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"

html = engine.get(URL)

doc = xpath.Doc(html)

pizzerie = [ x[15:] for x in doc.search("//a[@class='_lms _noc']/@title")]

tel = doc.search("//div[@class='tel']/span[@class='value']/text()")
address = doc.search("//div[@class='address']/span[@class='street-address']/text()")

info = zip(tel,address)

elenco_tel = dict(zip(pizzerie,info))

import re
def cerca(cosa):
    match = filter(lambda x: re.search(cosa,x,re.I), elenco_tel)
    for p in match:
        print p,":",' - '.join(elenco_tel[p])

cerca('pizz')
