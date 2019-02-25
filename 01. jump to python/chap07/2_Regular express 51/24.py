import re

data = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/" \
       "odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

p = re.compile('/(\d{4})/0?(\d)/0?(\d)')
m = p.search(data)
print(m.group(1),m.group(2),m.group(3))


