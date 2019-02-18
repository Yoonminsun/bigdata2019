import re

p=re.compile('.') # '\n'을 제외한 모든 문자
                  # 문자열 클래스[.]로 사용한 경우 '.' 문자 자체를 의미하며
                  # 클래스가 아닌 '.'로 사용한 경우 '\n'을 제외한 모든 문자를 의미한다
m=p.match('1')
print('1.',m)
m=p.match('a')
print('2.',m)
m=p.match('K')
print('3.',m)
m=p.match(' ')
print('4.',m)
m=p.match('*')
print('5.',m)
m=p.match('''
123''')
print('6.',m)
m=p.match('\n3a!')
print('7.',m,'\n')

p=re.compile('...') # 첫번째,두번째,세번째글자가 각 '\n'을 제외한 모든 문자
m=p.match('dad')
print('1.',m)
m=p.match('hi! dad')
print('2.',m)
m=p.match('hi dad')
print('3.',m)
m=p.match('hi\ndad')
print('4.',m,'\n')

p=re.compile('da.') # 첫글자d, 두번째글자a, 세번째글자는 '\n'을 제외한 모든 문자
m=p.match('dad')
print('1.',m)
m=p.match('da!')
print('2.',m,'\n')

p=re.compile('da[.]') # 첫글자d, 두번째글자a, 세번째글자.
                      # 문자열 클래스 안([]) 에서 dot(.)을 사용하면 메타문자가 아닌 고유의 문자의 의미가 된다
m=p.match('dad')
print('1.',m)
m=p.match('da.')
print('2.',m,'\n')

p=re.compile('.',re.DOTALL) # DOTALL 옵션시 '\n'도 포함한 모든 문자를 의미한다
m=p.match('\n21a')
print('1.',m)
