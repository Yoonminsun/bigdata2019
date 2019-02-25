import re

p=re.compile('ab{3}')
m = p.search('ab')
print(m)
m = p.search('aabbbbbc')
print(m)
m = p.search('abbb')
print(m)
m = p.search('aabb')
print(m)