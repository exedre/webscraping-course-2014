import urllib2
from ntlm import HTTPNtlmAuthHandler

user = '<user>'
password = "<oassword>"
url = "http://intranethome/locali/studi/cs/Documenti%202011/Salani%C3%A9_10%20gennaio.pdf"

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, user, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

import mechanize
browser = mechanize.Browser()
handlersToKeep = []

for handler in browser.handlers:
    if not isinstance(handler,
    (mechanize._http.HTTPRobotRulesProcessor)):
        handlersToKeep.append(handler)

browser.handlers = handlersToKeep
browser.add_handler(auth_NTLM)

response = browser.open(url)
print(response.read())



import mechanize

url = "http://<intranet>/locali/studi/cs/Documenti%202011/Salani%C3%A9_10%20gennaio.pdf"
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)'), ('Authorization', 'Basic %s:%s' % ('UTENZE\\<password>', '<user>'))]
r = br.open(url)
html = r.read()



