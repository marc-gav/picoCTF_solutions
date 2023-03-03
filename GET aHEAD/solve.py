import regex
from pprint import pprint as pp
import requests

url = 'http://mercury.picoctf.net:53554/'

# POST HEAD request to get the flag
r = requests.head(url, allow_redirects=False)
content = r.headers

# Find the flag
flag = regex.findall(r'picoCTF{.*}', content['flag'])[0]
print(flag)