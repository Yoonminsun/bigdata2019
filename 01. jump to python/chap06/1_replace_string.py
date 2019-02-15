f = open('./learning_python.txt','r')
fp = f.tell()
open_text = f.read()
f.seek(fp)
open_text_print = f.readlines()
for i in open_text_print:
    if i=='\n':
        continue
    print(i.strip())
f.close()

f = open('./learn_python_copyed.txt','w')
write_text = open_text.replace('python','C')
f.write(write_text)
f.close()

f = open('./learn_python_copyed.txt','r')
write_text_print = f.readlines()
for i in write_text_print:
    if i=='\n':
        continue
    print(i.strip())
f.close()


