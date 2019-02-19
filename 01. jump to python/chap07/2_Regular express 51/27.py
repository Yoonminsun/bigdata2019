import re

data = "Ten 10, Twenty 20, Thirty 30"

p = re.compile('\d+')
m=p.findall(data)
print(m)

