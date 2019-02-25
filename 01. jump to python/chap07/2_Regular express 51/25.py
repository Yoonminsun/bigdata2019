import re

data = '2018-02-19'
p = re.compile('(\d{4})-(\d{2})-(\d{2})')
m = p.sub('\g<3>-\g<2>-\g<1>',data)
print(m)

