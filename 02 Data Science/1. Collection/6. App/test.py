from urllib.request import Request,urlopen
from urllib.parse import urlencode,quote_plus
import json

access_key='oQSz2oLeE2%2FyKkC5Bvap%2ByKJ7NjXePjiinT9FimEL9PX9o0aEMHImBYj3NVIi9ArzQx4avj62hoXKqANLvj%2FcA%3D%3D'
sidoName = '대구'

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): access_key, quote_plus('numOfRows'): '100', quote_plus('pageNo'): '1',
         quote_plus('sidoName'): sidoName})

request = Request(url+queryParams)
request.get_method = lambda :'GET'
response_body = urlopen(request).read().decode('utf8')
print(url+queryParams)
print(response_body)
print(json.loads(response_body))