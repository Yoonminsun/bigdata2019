import re

p=re.compile('^[a-z]+[_][a-z]+$')
m = p.search('aab_cbbbc')
print(m)
m = p.search('aab_Abbbc')
print(m)
m = p.search('Aaab_abbbc')
print(m)
m = p.search('aabbbbc')
print(m)