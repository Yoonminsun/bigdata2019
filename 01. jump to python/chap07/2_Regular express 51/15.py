import re

p=re.compile('^3')
m = p.search('3ddA2_2')
print(m)
m = p.search('ddA2_2')
print(m)
