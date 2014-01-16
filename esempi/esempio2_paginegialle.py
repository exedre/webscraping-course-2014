import requests
URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"
data = requests.get(URL)
html = data.content


from lxml.html import fromstring
dom = fromstring(html)

links_c = dom.cssselect("a._lms._noc")
links_x = dom.xpath("//a[@class='_lms _noc']")


links_c == links_x

N = len("Scheda Azienda ")

pizzerie_2 = [ link.attrib['title'][N:] for link in links_c ]
