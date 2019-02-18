import re

print('?')
p = re.compile('ab?c') # a, b{0,1}, c -> ac,abc 가 매칭 되야함
m=p.match('ac') # ac
print('1.',m)
m=p.match('abc') # abc
print('2.',m)
m=p.match('abbc')
print('3.',m)
m=p.match('abbbc')
print('4.',m)
m=p.match('abcd') # abc
print('5.',m)

print('*')
p = re.compile('\d*') # 숫자가 최소 0번부터 반복되는 경우
m=p.match('1')
print('1.',m)
m=p.match('12343')
print('2.',m)
m=p.match('')
print('3.',m,'\n')

print('+')
p = re.compile('\d+') # 숫자가 최소 1번부터 반복되는 경우
m=p.match('1')
print('1.',m)
m=p.match('12343')
print('2.',m)
m=p.match('')
print('3.',m,'\n')

print('file.txt')
p = re.compile('file[0-9]{1,3}.txt') #file+숫자로 이루어진 text 파일중 100번대 까지 찾고 싶을때
m=p.match('file.txt')
print('1.',m)
m=p.match('file1.txt')
print('2.',m)
m=p.match('file23.txt')
print('3.',m)
m=p.match('file326.txt')
print('4.',m)
m=p.match('file4251.txt')
print('5.',m)
m=p.match('file@32.txt')
print('5.',m,'\n')

