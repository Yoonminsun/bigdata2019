import re

data =  '\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m'

p=re.compile('\\t|\\x1b\[0;?[a-z]+') # [[] 는 FutureWarining을 발생시키므로 \[으로 사용하면 된다
m=p.sub('',data)
print(m)
