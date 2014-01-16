import requests
URL =  "http://roma.paginegialle.it/lazio/roma/pizzeria.html"
data = requests.get(URL)
html = data.content


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)

pizzerie_3 = [ re.sub('^Scheda Azienda ','',h2['title']) for h2 in soup.findAll('a', attrs={'class': '_lms _noc'})]



