import requests
import hashlib
from urllib.request import urlopen, Request

html_text = requests.get('https://asdk.ru/services/test.php').text
# print(html_text)
# a href="/about/">О компании </a></td>
hash_object = hashlib.md5(html_text.encode('utf-8')).hexdigest()
print(hash_object)

response_url = urlopen('https://asdk.ru/services/test.php').read()
#print(response_url)
#/library/19/204">\xd0\xe0\xe7\xed\xe8\xf6\xe0 \xec\xe5\xe6\xe4\xf
current_hash = hashlib.md5(response_url).hexdigest()
print(current_hash)