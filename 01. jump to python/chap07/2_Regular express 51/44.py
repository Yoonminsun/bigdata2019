import re

data =  'PHP exercise'

p=re.compile('php',re.IGNORECASE)
m=p.sub('Python',data)
print(m)
