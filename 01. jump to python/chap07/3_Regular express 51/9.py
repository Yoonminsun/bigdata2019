import re

p=re.compile('a.*b$')
m = p.search('aabbbbd')
print(m)
m = p.search('aabAbbbc')
print(m)
m = p.search('accddbbjjjb')
print(m)
