import sys
import urllib
from bs4 import BeautifulSoup
import json



def getTimes(query,num):
    url = "http://query.nytimes.com/svc/cse/v2/sitesearch.json?query="+query.replace(" ","%20")+"&pt=article&page="+str(num)
    jtext = urllib.urlopen(url)
    return jtext

def search(term):
    page_number = 0
    meta = 1
    while meta > 0 and page_number<1:
        gt = getTimes(term,page_number)
        resp = json.load(gt)
        meta = int(resp['results']['meta']['payload']) 
        for res in resp['results']['results']:
            print res['snippet']
            headline = res['hdl']
            #snippet = res['snippet']
            #author = res['cre']
            url = res['url']
            print headline.encode('utf-8')
            print url  
        page_number+=1            

keyword = sys.argv[1]
search(keyword)


