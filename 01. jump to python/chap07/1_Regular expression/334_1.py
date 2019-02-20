import re

p = re.compile('a[.]{3,}b')
m = p.search('a....b')
print(m)