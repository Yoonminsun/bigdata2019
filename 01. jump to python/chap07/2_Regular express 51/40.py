import re

data = 'Python      Exe rcises'

p=re.compile('\s')
print(p.sub('',data))


