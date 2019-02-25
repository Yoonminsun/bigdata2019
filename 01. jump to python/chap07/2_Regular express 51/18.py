import re

data = 'Exercises number 1, 12, 13, and 345 are important'
p=re.compile('\d{1,3}')
m = p.findall(data)
print(m)
