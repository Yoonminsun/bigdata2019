import re

p=re.compile('^\w+')
m = p.search('The quick brown.')
print(m)
m = p.search(' The quick brown.')
print(m)
m = p.search('@The quick brown.')
print(m)
