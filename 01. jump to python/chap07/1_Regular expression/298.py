import re

# match() 함수는 무조건 첫글자부터 위치에 맞게 있어야 매칭 되고, search() 함수는 문자열 안에 위치만 맞게 있다면 매칭 된다
# var1 = re.compile('정규식')
# var2 = var1.match('문자열')
# var2 = var1.search('문자열')

p=re.compile('[abc]') # a,b,c
m=p.match('a') # 첫글자가 a 이므로 매칭O
print(m)
m=p.match('k') # 첫글자가 k 이므로 매칭X
print(m)
m=p.match('before') # 첫글자가 b 이므로 매칭O
print(m)
m=p.match('dude') # 첫글자가 d 이므로 매칭X
print(m)
m=p.match('ebfore') # b가 있지만 첫글자가 아니라서 매칭X
print(m)

p=re.compile('a[poi]') # 두글자 연속 ap,ao,ai
m=p.match('apple') # 처음부터 두글자가 ap 이므로 매칭O
print(m)
m=p.match('abs') # a는 매칭되지만 뒷글자가 매칭되지 않아 매칭X
print(m)
m=p.search('pad') # a,p 가 있지만 Search 라도 위치가 다르기 때문에 매칭X
print(m)
m=p.search('baic') # Search 이므로 첫글자부터 시작할 필요없고, ai 위치가 순서대로 있기때문에 매칭O
print(m)

p=re.compile('[abc]d') # 두글자 연속 ad,bd,cd
m = p.match('dad') # ad가 문자열 안에 있으나, match()함수는 첫글자부터 있어야 하는데 두번째부터 있으므로 매칭X
print(m)

p=re.compile('[cd][ab]') # 두글자 연속 ca,cb,da,db
m = p.match('da') # 첫글자부터 da가 있으므로 매칭O
print(m)