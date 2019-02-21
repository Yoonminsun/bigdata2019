import re

data =  '\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m'

'\t'
'\u001b[0;35m'
'\u001b[0m'
'\u001b[0;36m'
'\u001b[0m'

p=re.compile('[\][a-z]\d*[a-z][\d;?\d*[a-z]')
# m=p.sub('**',data)
n = p.findall(data)
# print(m)
print(n)
