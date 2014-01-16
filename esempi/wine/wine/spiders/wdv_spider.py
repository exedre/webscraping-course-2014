from pprint import pprint

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

import re

from wine.items import WineItem

class WDVSpider(BaseSpider):
    name = "wdv"
    allowed_domains = ["webdivino.com"]
    start_urls = [
        'http://www.webdivino.com/prodotti.asp?cat=11',
        'http://www.webdivino.com/prodotti.asp?cat=12',
    ]

    def parseSched(self, response):
        sel = HtmlXPathSelector(response)
        names = filter(lambda x: len(x.strip())>0, sel.select("//td[@class='txtGenRicerca']/text()").extract())
        value = filter(lambda x: len(x.strip())>0, sel.select("//td[@class='totCarrello']/text()").extract())
        items = []
        item = WineItem()
        prodotto = sel.select("//td[@class='bannerHead']/strong/text()").extract()
        item[u'Prodotto']=prodotto[0].strip()
        for n,v in zip(names,value):
            k = re.sub(':','',n)
            if re.match('Prezzo',k):
                v = re.sub(',','.',v.split()[0])
            item[k]=v.strip()
        yield item
        
    def parse(self, response):
        sel = HtmlXPathSelector(response)
        trP = int(sel.select('//tr[@class="vociAcquista"]/td[@align="left"]/text()').extract()[0].split()[3])
        for i in range(1,trP+1):
            url = response.url + "&pagina=%d" % i
            yield Request(url, callback=self.parseList) 

    def parseList(self,response):
        sel = HtmlXPathSelector(response)
        names = filter(lambda x: len(x.strip())>0, sel.select("//td[@class='txtConRicerca']/text()").extract())
        euros = filter(lambda x: len(x.strip())>0, sel.select("//td[@class='txtConRicerca']/span/text()").extract())
        sched = filter(lambda x: not re.match("^add_",x), sel.select("//td[@class='txtGenRicerca']/a/@href").extract())
        
        for n,e,s in zip(names,euros,sched):        
            url = 'http://www.webdivino.com/%s'
            yield Request(url % s, callback=self.parseSched) 
