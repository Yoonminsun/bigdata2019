import re
original_text = 'life is too short'
p = re.compile('[a-z]+')

m=p.finditer(original_text) # finditer 은 match 객체를 iterator 객체로 리턴
for i in m:
    print(i) # 각각은 match 객체 이므로
    print(i.group()) # group() 함수를 사용하면 매칭된 문자열만 뽑아낼 수 있음
