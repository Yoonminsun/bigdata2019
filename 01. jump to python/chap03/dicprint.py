dic = {1:'a',2:'b',3:'c',4:'d'}

klist = list(dic.keys())
vlist = list(dic.values())

for i in klist:
	for j in vlist:
            print("%-3s :  %-3s"%(i,j),end='/')
	print("\n")
