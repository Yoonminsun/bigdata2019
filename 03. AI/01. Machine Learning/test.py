import pandas as pd
import random,re

## DataFrame 으로 읽어들인 후 리스트로 만들어 shuffle 하기
house = pd.read_csv('Housing.csv',sep=',',header=0)
house_list=[]
for num in range(len(house)):
    data=[]
    for num2 in range(len(house.values[num])):
        data.append(house.values[num][num2])
    house_list.append(data)
random.shuffle(house_list)


# random.shuffle(house)
# total_len = len(house)
# train_len = int(total_len * 2/3)
# house = house.loc[0:train_len,'price']
# house = house.loc[train_len+1:total_len,'price']
# print(house)