import re

data = 'The quick brown fox jumps over the lazy dog.'
p=re.compile('(?=fox|dog|horse)\w*')
m = p.findall(data)
print(m)
