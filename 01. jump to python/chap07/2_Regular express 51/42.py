import re

data =  '<p>Contents :</p><a href="https://w3resource.com">' \
        'Python Examples</a><a href="http://github.com">Even More Examples</a>'

p=re.compile('href="(.+)">')
m=p.finditer(data)
for i in m:
    print(i.group(1))


