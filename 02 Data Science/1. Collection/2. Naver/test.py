import re

data = 'http://blog.naver.com/nakhkh?Redirect=Log&amp;logNo=221408425667'

p = re.compile('.+logNo=(\d+)')
m = p.sub('\g<1>',data)
print(m)