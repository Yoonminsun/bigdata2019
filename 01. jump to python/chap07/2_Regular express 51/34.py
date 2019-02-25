import re

data = 'The quick brown fox jumps over the lazy dog'

p = re.compile('\w{3,5}')
m=p.findall(data)
print(m)

