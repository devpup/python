# import urllib
# url = "https://google.com"
# html = urllib.urlopen(url).read()
# print(html)

import ssl
import urllib

url = "https://google.com"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.urlopen(url, context=ctx).read()
print(html.decode('utf-8').encode('euc-kr'))