f=open('./source.txt','r')

source = f.read()
source_copy = source.replace("\t","    ")
f.close()
f=open('./source.txt','w')
f.write(source_copy)
f.close()