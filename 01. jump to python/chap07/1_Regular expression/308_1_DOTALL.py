import re
original_text='a\nb'

# p=re.compile('a.b') # dot(.)을 메타문자로 사용시 기본은 '\n' 을 제외한 모든 문자를 매칭
p=re.compile('a.b',re.DOTALL) # DOTALL 옵션을 사용하면 dot(.)을 메타문자로 사용할때 '\n'도 매칭문자에 포함
                              # dot을 사용하지 않고 '\n'을 매칭하려면 정규식에 '\n' 자체를 적어주면 된다
m = p.match(original_text)
print(m)
