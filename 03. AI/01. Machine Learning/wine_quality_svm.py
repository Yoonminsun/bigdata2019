# 고정변수값 예측하기
import pandas as pd
from statsmodels.formula.api import ols,glm
import operator
from itertools import combinations
from datetime import datetime
from sklearn import svm,metrics

print("< Winequality Predict Svm >")

wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

colums_list = ['alcohol','chlorides','citric_acid','density','fixed_acidity','free_sulfur_dioxide','pH',
               'residual_sugar','sulphates','total_sulfur_dioxide','volatile_acidity']
wine_label = wine['quality']
wine_data = wine[colums_list]

clf = svm.SVC(gamma='auto')
clf.fit(wine_data,wine_label)
pre = clf.predict(wine_data)

ac_score = metrics.accuracy_score(wine_label,pre)
print('전체 조합 정답률: %.2f %%'%(ac_score*100)) ## 79.73%

match_dic={}

for num in range(1,len(colums_list)+1):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        wine_data = wine[list(tup)]
        clf = svm.SVC(gamma='auto')
        clf.fit(wine_data,wine_label)
        pre = clf.predict(wine_data)
        ac_score = metrics.accuracy_score(wine_label,pre)
        combi_str = '+'.join(list(tup))
        print('\n>> 조합: %s'%(combi_str.rstrip('+')))
        print('>> 정답률: %.2f %%'%(ac_score*100))
        match_dic['%s'%(combi_str.rstrip('+'))] = ac_score*100

match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))




