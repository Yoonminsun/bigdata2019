from xml.etree.ElementTree import parse
import re

menu=0
tree = parse('students_info.xml')
note = tree.getroot()

p = re.compile('\s+')
p_num = re.compile('\d+')
text_list = list(note.itertext())
for text in text_list:
    m=p.match(text)
    m_num = p_num.match(text)
    if not m and m_num:
        print('age: '+text)
    elif not m and not m_num:
        print('major: '+text)