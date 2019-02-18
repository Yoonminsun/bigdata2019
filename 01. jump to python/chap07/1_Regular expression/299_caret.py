import re

p = re.compile('[^0]') # 0이 아닌 문자
m=p.match('1')
print('1.',m)
m=p.match('0') # 첫글자가 0이므로 매칭X
print('2.',m)

p=re.compile('[^0-9]') # 숫자(0~9)가 아닌 문자
m=p.match('1')
print('3.',m)

p=re.compile('^0') # ^(caret)은 문자열 클래스 안([])에서만 not으로 통용된다
m=p.match('1')
print('4.',m)

p=re.compile('^') # ^ 문자
m=p.match('^0')
print('5.',m)

p=re.compile('[^a-zA-Z0-9]') # a~z, A~Z, 0~9 가 아닌 문자, 즉 문자+숫자가 아닌 문자
m=p.match('7')
print('6.',m)

p=re.compile('[^a-zA-Z09]') # a~z, A~Z, 0,9 가 아닌 문자
m=p.match('9')
print('7.',m)
m=p.match('8')
print('8.',m)


