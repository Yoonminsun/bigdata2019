import re
original_text='''sdfsdgsdgsd
3sdgwejoirjwoerijw
'''

# p=re.compile('[a-z]*.3[a-z]*')
# '\n'이 매칭되지 않는데 3은 다음줄에 있으므로 매칭X

p=re.compile('[a-z]*.3[a-z]*',re.DOTALL)
# '\n'이 매칭되는 옵션이므로, .이 '\n'에 매칭되고 다음줄 3이 그대로 3에 매칭되서 매칭O

m = p.match(original_text)
print(m)
