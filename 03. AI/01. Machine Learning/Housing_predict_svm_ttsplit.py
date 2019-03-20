import pandas as pd
import numpy as np
from itertools import combinations
import operator
from sklearn import svm,metrics
from sklearn.model_selection import train_test_split

print("< Housing Predict Svm >")
house = pd.read_csv('Housing.csv',sep=',',header=0)
columns_change = ['driveway01','recroom01','fullbase01','gashw01','airco01','prefarea01']
columns_ori = ['driveway','recroom','fullbase','gashw','airco','prefarea']

for index in range(len(columns_ori)):
    house[columns_change[index]] = np.where(house[columns_ori[index]] == 'yes', 1, 0)

independent_variables_list = ['lotsize','bedrooms','bathrms','stories','driveway01','recroom01','fullbase01','gashw01','airco01',
                'garagepl','prefarea01']

house_label = house['price']
match_dic_0={}
match_dic_5={}
match_dic_10={}
match_dic_20={}
delta_plus = lambda x,y:x+x*y
delta_minus = lambda x,y:x-x*y

## metrics 사용
# for num in range(1,len(independent_variables_list)+1):
#     combi_list = list(combinations(independent_variables_list,num))
#     for tup in combi_list:
#         house_data = house[list(tup)]
#         clf = svm.SVC(gamma='auto')
#         clf.fit(house_data,house_label)
#         pre = clf.predict(house_data)
#         ac_score = metrics.accuracy_score(house_label,pre)
#         combi_str = '+'.join(list(tup))
#         print('\n>> 조합: %s' % (combi_str.rstrip('+')))
#         print('>> 정답률: %.2f %%' % (ac_score * 100))
#         match_dic_5['%s' % (combi_str.rstrip('+'))] = ac_score * 100
#
# match_dic_5 = sorted(match_dic_5.items(), key=operator.itemgetter(1),reverse=True)
# print('총 조합 갯수: %d'%len(match_dic_5))
# print("MAX 조합: %s >> %.2f %%"%(match_dic_5[0][0],match_dic_5[0][1]))

## delta 범위 지정
for num in range(1,len(independent_variables_list)+1):
    combi_list = list(combinations(independent_variables_list,num))
    for tup in combi_list:
        house_data = house[list(tup)]
        train_data, test_data, train_label, test_label = train_test_split(house_data, house_label)
        clf = svm.SVC(gamma='auto')
        clf.fit(train_data,train_label)
        pre = clf.predict(test_data)
        match_count_0=0
        match_count_5=0
        match_count_10=0
        match_count_20=0
        for index in range(len(pre)):
            ### 0%
            if pre[index] == house_label[index]:
                match_count_0+=1
            ### 5%
            if delta_minus(house_label[index], 0.05) < pre[index] < delta_plus(house_label[index], 0.05):
                match_count_5 += 1
            ### 10%
            if delta_minus(house_label[index], 0.1) < pre[index] < delta_plus(house_label[index], 0.1):
                match_count_10 += 1
            ### 20%
            if delta_minus(house_label[index], 0.2) < pre[index] < delta_plus(house_label[index], 0.2):
                match_count_20 += 1
        combi_str = '+'.join(list(tup))
        print('\n>> 조합: %s'%(combi_str.rstrip('+')))
        print('>> 0% match count=',match_count_0)
        print('>> 5% match count=',match_count_5)
        print('>> 10% match count=', match_count_10)
        print('>> 20% match count=', match_count_20)
        print('>> 0%% 정답률: %.2f %%'%(match_count_0/len(pre)*100))
        print('>> 5%% 정답률: %.2f %%'%(match_count_5/len(pre)*100))
        print('>> 10%% 정답률: %.2f %%' % (match_count_10 / len(pre) * 100))
        print('>> 20%% 정답률: %.2f %%' % (match_count_20 / len(pre) * 100))
        match_dic_0[combi_str] = match_count_0/len(pre)*100
        match_dic_5[combi_str] = match_count_5/len(pre)*100
        match_dic_10[combi_str] = match_count_10 / len(pre) * 100
        match_dic_20[combi_str] = match_count_20 / len(pre) * 100

match_dic_0 = sorted(match_dic_0.items(),key=operator.itemgetter(1),reverse=True)
match_dic_5 = sorted(match_dic_5.items(),key=operator.itemgetter(1),reverse=True)
match_dic_10 = sorted(match_dic_10.items(),key=operator.itemgetter(1),reverse=True)
match_dic_20 = sorted(match_dic_20.items(),key=operator.itemgetter(1),reverse=True)
print("전체 데이터 수: %d"%(len(house)))
print("학습 데이터 수: %d"%(len(train_data)))
print("테스트 데이터 수: %d"%(len(test_data)))
print('0%% MAX 조합: %s >> %.2f %%'%(match_dic_0[0][0],match_dic_0[0][1]))
print('5%% MAX 조합: %s >> %.2f %%'%(match_dic_5[0][0],match_dic_5[0][1]))
print('10%% MAX 조합: %s >> %.2f %%'%(match_dic_10[0][0],match_dic_10[0][1]))
print('20%% MAX 조합: %s >> %.2f %%'%(match_dic_20[0][0],match_dic_20[0][1]))