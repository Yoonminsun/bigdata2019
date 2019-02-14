def check(num):
    for i in num:
        if num.count(i) >1:
            return 'false'
    return 'true'

num_list = input("입력: ").split(' ')

for i in num_list:
    print(check(i),end=' ')



