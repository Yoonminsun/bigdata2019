def check(num):
    for i in range(10):
        check_num = num.count(str(i))
        if check_num >1 or check_num==0:
            return 'false'
    return 'true'

num_list = input("입력: ").split(' ')
# Testcase
# 0123456789 01234 01234567890 6789012345 012322456789

for i in num_list:
    print(check(i),end=' ')



