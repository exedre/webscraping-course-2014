from webscraping import download, xpath

engine = download.Download()

html = engine.get('http://code.google.com/p/webscraping')

project_title = xpath.get(html, '//div[@id="pname"]/a/span')

labels = xpath.get(html, '/a[@class="label"]')
