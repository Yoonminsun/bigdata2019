import re

data = 'Python      Exercises'

p=re.compile(' {2,}')
print(p.sub(' ',data))


