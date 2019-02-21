from xml.etree.ElementTree import Element,SubElement,dump,ElementTree

note = Element('note')
note.attrib["date"] = "20120104"

to = Element('to')
# to.text = "Tove"
note.append(to)

SubElement(note, 'from').text = 'Jani'
SubElement(note,'heading').text = 'Reminder'
SubElement(note, 'body').text = "Don't forget me this weekend!"

# note text=None tail=None
# date text=20120104 tail=None
# to text=None tail=None
# from text=Jani tail=None
# heading text=Reminder tail=None
# body text=Don't forget me this weekend! tail=None

def indent(elem, level=0):
    # 메모장에서 줄바꿈하는것과 달리 프로그램내에서 줄바꿈할시 앞 줄의 들여쓰기를 그대로 유지하지 않기 때문에 level이 필요한 것
    i='\n' + level*' '
    if len(elem): # Element의 length는 하위 Element의 갯수를 뜻한다
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem,level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)

ElementTree(note).write('note.xml')

