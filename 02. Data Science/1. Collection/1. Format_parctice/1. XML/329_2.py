from xml.etree.ElementTree import Element,dump,SubElement

note = Element('note')

to = Element('to')
to.text = "Tove"
note.append(to)

SubElement(note,"from").text = 'Jani'

note.attrib["date"] = "20120104" # 속성(attribuete)추가
                                 # 부모Element.attrib["속성명"] = "속성값"
dump(note)



