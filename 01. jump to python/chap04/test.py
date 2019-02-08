f = open('test.txt','w')
for i in range(1,6):
    f.write('%d번째 '%i)

f.close()


f = open('test.txt','r')

for line in f.readlines():
    print(line)

f.close()