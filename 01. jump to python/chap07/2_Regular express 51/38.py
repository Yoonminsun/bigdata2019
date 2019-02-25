import re

data = '"Python", "PHP", "Java"'

p=re.compile('".+"')
m=p.findall(data)
print(m)


