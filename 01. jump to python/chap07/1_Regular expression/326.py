import re
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())
print(re.match('<.*>',s).group())
print(re.match('<.*?>',s).group()) # '?'는 가능한 한 가장 최소한의 반복을 수행하도록 도와준다
