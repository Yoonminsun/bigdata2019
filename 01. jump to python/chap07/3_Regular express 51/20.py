import re

data = 'The quick brown fox jumps over the lazy dog.'
p=re.compile('(?=fox)\w*')
m = p.search(data)
print(m.group())
print(m.span())
