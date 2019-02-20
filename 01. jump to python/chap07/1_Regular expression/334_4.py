import re

data = '''
park@naver.com
kim@daume.net
lee@myhome.co.kr
'''

p = re.compile('.*[@].*[.](?=com|net).*$',re.MULTILINE)
m = p.findall(data)
print(m)