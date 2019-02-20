import re

p=re.compile('ab+')
m = p.search('ab')
print(m)
m = p.search('abc')
print(m)
