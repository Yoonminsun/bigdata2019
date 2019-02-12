f=open('test_read_split.txt','r',encoding='UTF-8')
name_list = []
price_list = []
for line in f:
    name, price = line.strip().split(' ')
    name_list.append(name)
    price_list.append(price)

print(name_list, price_list ,sep='\n')

# 파일 읽어와 split 하여 각각 list에 저장하기