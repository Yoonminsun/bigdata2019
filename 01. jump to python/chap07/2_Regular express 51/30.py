import re

data = '21 Ramkrishna Road'

p = re.compile('Road')
print(p.sub('Rd.',data))

