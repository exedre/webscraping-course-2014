import mechanize
br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

import cookielib
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


r = br.open('http://google.com')
html = r.read()


# Show the html title
print br.title()

# Show the available forms
for f in br.forms():
    print f

# Select the first (index zero) form
br.select_form(nr=0)

# Let's search
br.form['q']='data science'
r = br.submit()

html = r.read()

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html)

nres = soup.find('div',attrs={'id':'resultStats'}).text

wlinks =  [ w for w in br.links(url_regex='wikipedia') ]

# Looking at some results in link format
for l in wlinks:
    print l.url

w0 = wlinks[0]
    
r = br.open(w0.url)
    
print br.title()
print br.geturl()


html = r.read()

soup = BeautifulSoup(html)

a_li = soup.select('.interlanguage-link')

print ('\n'.join([ li.a['lang']+" "+li.text for li in a_li])).encode('utf-8')


