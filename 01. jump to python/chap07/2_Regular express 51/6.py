import re

p=re.compile('ab{2,3}')
m = p.search('ab')
print(m)
m = p.search('abb')
print(m)
m = p.search('abbb')
print(m)
m = p.search('aabbbbc')
print(m)