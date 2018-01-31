from os.path import join
from webscraping import download, xpath
from lxml.html import fromstring

URL =  "/Volumes/MULETTO/"

h={}
for f in [ "2011","2012","2013","PRE"]:
    html = open(join(URL,f)+".html",'r').read()
    dom = fromstring(html)
    sbox = dom.xpath("//div[@class='midbox4']")
    data1 = [ s.xpath(".//div[@class='b1' or @class='c3a']/text()") for s in sbox ]
    data2 = [ s.xpath(".//div[@class='c3b']/text()") for s in sbox ]
    data3 = [ s.xpath(".//div[@class='c3b']/a/@href") for s in sbox ]
    info = zip(data1,data2,data3)    
    h[f]=info
        
HH = []
for l,v in h.items():
    for nn in v:
        VH = []
        VH.append(l)
        for w in nn:
            VH.extend(w)
        HH.append(VH)

for h in HH:
    print " | ".join([ k.encode('utf8','ignore') for k in h])
    
pizzerie = [ x[15:] for x in doc.search("//a[@class='_lms _noc']/@title")]

tel = doc.search("//div[@class='tel']/span[@class='value' o]/text()")
address = doc.search("//div[@class='address']/span[@class='street-address']/text()")

info = zip(tel,address)

elenco_tel = dict(zip(pizzerie,info))

import re
def cerca(cosa):
    match = filter(lambda x: re.search(cosa,x,re.I), elenco_tel)
    for p in match:
        print p,":",' - '.join(elenco_tel[p])

cerca('pizz')
