my_str = 'aaabbcccccca'
current_chr=my_str[0]
count=1
result=my_str[0]

for i in range(1,len(my_str)):
    if current_chr==my_str[i]:
        count+=1
    if current_chr!=my_str[i]:
        current_chr=my_str[i]
        result = result + str(count) + my_str[i]
        count=1
    if count==1 and i==len(my_str)-1:
        result += '1'

print(result)

