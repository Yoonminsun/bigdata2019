import re

p=re.compile('\w+\S*$')
m = p.search('The quick brown.')
print(m)
m = p.search('The quick brown. ')
print(m)
m = p.search('@The quick brown')
print(m)
