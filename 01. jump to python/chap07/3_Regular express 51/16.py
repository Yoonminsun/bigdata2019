import re

data = '216.08.094.196'
p=re.compile('0*(\d*)')
m = p.sub('\g<1>',data)
print(m)
