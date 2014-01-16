#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests

results = {}

companies = sys.argv[1:]

for company in companies:
    url = "http://www.linkedin.com/company/{}".format(company)  
    raw = requests.get(url).content

    soup = BeautifulSoup(raw)

    node = soup.find(attrs = {"class" : "grid-f"})

    if node!=None:
        info = node.find(attrs = {"class" : "basic-info"})
        titles = [item.get_text(strip=True) for item in info.findAll("dt")]
        data = [item.get_text(strip=True) for item in info.findAll("dd")]    
        output = dict(zip(titles,data))
    else:
        output = {}
        
    output['company'] = company    
    results[company] = output

    import random, time
    sleep_time = random.uniform(5,10)
    time.sleep(sleep_time)

import json
print json.dumps(results, indent=2)    
