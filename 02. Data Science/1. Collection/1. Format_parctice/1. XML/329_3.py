from xml.etree.ElementTree import Element,dump,SubElement,ElementTree

# attrib 함수 사용 없이 속성으로 추가하는 법(생성시 바로), 여러개 가능
note = Element('note',data="20120104",to="Tove")

# to = Element('to')
# to.text = "Tove"
# note.append(to)

SubElement(note,"from").text = 'Jani'

dump(note)


ElementTree(note).write('note.xml') # xml 파일로 바로 변환(쓰기) 가능한 함수
