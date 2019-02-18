import re
# 아래 표기법은 하나를 예로 '[\d]'로 표기할 수 있지만, '\d'로도 가능하다
p = re.compile('[\d]') # 숫자
m=p.match('1')
print('1.',m)
m=p.match('5')
print('2.',m,'\n')

p = re.compile('[\D]') # 숫자가 아닌 문자
m=p.match('1')
print('1.',m)
m=p.match('a')
print('2.',m,'\n')

p = re.compile('[\s]') # whitespace 문자, [ \t\n\r\f\v]
m=p.match(' 2')
print('1.',m)
m=p.match('3 ')
print('2.',m)
m=p.match('\nabc')
print('3.',m)
m=p.match('''
123''') # multiline 으로 \n 표현
print('4.',m,'\n')

p = re.compile('[\S]') # whitespace 문자가 아닌 문자, [^ \t\n\r\f\v]
m=p.match(' 2')
print('1.',m)
m=p.match('3 ')
print('2.',m)
m=p.match('\nabc')
print('3.',m)
m=p.match('''
123''')
print('4.',m,'\n')

p = re.compile('[\w]') # a~z+A~Z+숫자
m=p.match('a23')
print('1.',m)
m=p.match('3ab4')
print('2.',m)
m=p.match('$23')
print('3.',m,'\n')

p = re.compile('[\W]') # a~z+A~Z+숫자 가 아닌 문자
m=p.match('a23')
print('1.',m)
m=p.match('3ab4')
print('2.',m)
m=p.match('!23')
print('3.',m,'\n')
