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

print("- Regular expression : '.*[.].*$'")
p = re.compile('.*[.].*$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')

# 확장자가 bat인 파일은 제외해야하는 조건 추가
print("- Regular expression : '.*[.][^b].*$'")
p = re.compile('.*[.][^b].*$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')

# 확장자의 길이가 3임을 전제로 하기 때문에 cf 까지 필터링 됨
print("- Regular expression : '.*[.]([^b]..|.[^a].|..[^t])$'")
p = re.compile('.*[.]([^b]..|.[^a].|..[^t])$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')

# 확장자의 길이가 2이상이되도록 '?'를 추가하여 bat만 필터링되나 너무 복잡해짐
print("- Regular expression : '.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$'")
p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search('m.bpat') # 완벽히 bat만 필터링되는게 아님
print(m)
m = p.search(cf)
print(m,'\n')

# 부정형 전방 탐색 이용하여 간략해진 정규식
print("- Regular expression : '.*[.](?!bat).*$'")
p = re.compile('.*[.](?!bat).*$')
m = p.search(bar)
print(m)
m = p.search(bat)
print(m)
m = p.search(cf)
print(m,'\n')
