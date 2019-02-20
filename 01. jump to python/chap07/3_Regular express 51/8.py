import re

p=re.compile('^[A-Z][a-z]+$')
m = p.search('aab_cbbbc')
print(m)
m = p.search('Aabcc123')
print(m)
m = p.search('aaBcc!')
print(m)
