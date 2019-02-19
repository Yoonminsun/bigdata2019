import re

data = 'Python Exercises, PHP exercises.'

p = re.compile('[., ]')
print(p.sub(':',data,count=2))

