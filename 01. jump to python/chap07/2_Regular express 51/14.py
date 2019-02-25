import re

p=re.compile('^[\w_]*$')
m = p.search('ddA2_2')
print(m)
m = p.search('dd!A2_2')
print(m)
