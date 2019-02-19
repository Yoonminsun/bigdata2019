import re

p=re.compile('ab*')
m = p.search('ac')
print(m)
m = p.search('abc')
print(m)
m = p.search('abbc')
print(m)
