import re

data =  '<p>Contents :</p><a href="https://w3resource.com">' \
        'Python Examples</a><a href="http://github.com">Even More Examples</a>'

p=re.compile('[a-z]{4,5}://\w+.com')
m=p.findall(data)
print(m)


