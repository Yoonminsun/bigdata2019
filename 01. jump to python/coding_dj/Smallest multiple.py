num=2
sum=0
while True:
    for div in range(1,21):
        if num%div!=0:
            num += 2
            break
        elif div==20:
            print(num)
            exit()
