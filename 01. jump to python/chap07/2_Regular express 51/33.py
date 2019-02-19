import re

data = 'The quick brown fox jumps over the lazy dog'

p = re.compile('\w{5}')
m=p.findall(data)
print(m)

