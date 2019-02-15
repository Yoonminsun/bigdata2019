## 다른 사림이 짠 코드
# sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)})

## 집합을 활용하여 다시 짠 코드
num_set = set(range(5000))
gene=0
gene_set=set()
for i in range(5000):
    for j in str(i):
        gene+=int(j)
    gene+=i
    gene_set.add(gene)
    gene=0

print(sum(num_set - gene_set))


## 처음에 짠 코드_리스트 이용
# num_list=[]
# num=1
# n=1
# ans=0
#
# def generator(n):
#     result=0
#     for i in str(n):
#         result +=int(i)
#     result+=n
#     return result
#
# for i in range(1,5000):
#     num_list.append(i)
#
# while generator(n)<4999:
#     try:
#         del num_list[num_list.index(generator(n))]
#     except ValueError:
#         pass
#     n+=1
#
# for i in num_list:
#     ans+=i
# print(ans)
