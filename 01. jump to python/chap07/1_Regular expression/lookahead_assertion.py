import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
p = re.compile(".+(?=:)") # 긍정형 전방 탐색
m = p.search("http://google.com")
print(m.group())
print()

bar = 'foo.bar'
bat = 'autoexec.bat'
cf = 'sendmail.cf'

p = re.compile('.*[.].*$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
p = re.compile('.*[.][^b].*$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
p = re.compile('.*[.]([^b]..|.[^a].|..[^t])$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
p = re.compile('.*[.]([^b].*|.[^a].*|..*[^t])$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
p = re.compile('.*[.](?!bat).*$') # 부정형 전방 탐색
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
