from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note')# Element(태그명)

to = Element('to') # 자식노드
to.text = "Tove" # 현재 Element(태그)에 값 추가,
note.append(to) # 부모노드(note)에 자식노드(to) 추가

SubElement(note,"from").text = 'Jani' # SubElement를 활용하여 자식노드 추가 후 값 추가
# 9라인과 11,12,13 라인은 같은 결과이다(하위 개념일때)
# from_tag = Element('from')
# from_tag.text = 'Jani'
# note.append(from_tag)

dump(note) # note를 기준으로 하위를 보여줌



# 변수1 = Element('태그명')
# 변수2 = Element('태그명')   ==   SubElement(변수1(상위태그),"변수3의 태그명").text = '변수3의 값'
# 변수2.text = '값'
# 변수1.append(변수2)
