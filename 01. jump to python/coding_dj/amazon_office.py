time_list = ['09:12:23 11:14:35','10:34:01 13:23:40','10:34:31 11:20:10']
count=0
time = input("시간 입력: ")
hh_in, mm_in, ss_in = time.split(':')


for i in range(0,len(time_list)):
    time_1, time_2 = time_list[i].split(' ')
    hh_1,mm_1,ss_1 = time_1.split(':')
    hh_2,mm_2,ss_2 = time_2.split(':')
    time_1 = hh_1+mm_1+ss_1
    time_2 = hh_2+mm_2+ss_2
    time = hh_in+mm_in+ss_in

    if time>=time_1 and time<=time_2:
        count+=1

print("%d명"%count)

# 입력받는 시간들을 ':'을 빼고 숫자끼리 더하여 정수형으로 만든 후 특정 시간이 그 사이의 값인지 확인함
# 09:12:23 ~ 11:14:35 사이에 11:05:20 이 들어가는지 보려면
# 091223 과 111235 라는 수 사이의 범위인지 확인하면 됨 (24시간 체계로 표시하므로)




