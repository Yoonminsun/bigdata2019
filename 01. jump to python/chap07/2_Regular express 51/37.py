import re

data = 'python_exercises'

p=re.compile('(\w+)_(\w+)')
m=p.search(data)
print(m.group(1).capitalize(),m.group(2).capitalize())



