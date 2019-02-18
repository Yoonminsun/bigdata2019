import re
original_text='''a1 sdfsdgewgsfsdfsdf
b3 sdgowiejfsodkflsd
3k soegijslegikjselkgjsl
5j wieroqjrlsdkvmlsdflm
k4 qpwbmspblkspreopro
9p eorisjfl
u9 pbdjbldkjldkfld
'''

# p=re.compile('[a-z][0-9]') # 첫글자는 소문자 a~z 중, 두번째글자는 0~9 중에
# p = re.compile('[a-zA-Z][0-9]') # 첫글자는 소문자 a~z,대문자 A~Z 중, 두번째 글자는 0~9 중에
p = re.compile('[a-zA-Z0-9]') # 첫글자가 소문자 a~z, 대문자 A~Z, 숫자 중에
m=p.match(original_text) # 첫글자가 a1 이므로 매칭O
print(m)
if m:
    print("match found: ",m.group())

